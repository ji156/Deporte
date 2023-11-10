import scrapy
import requests
import psycopg2


class TablaSpider(scrapy.Spider):
    name = "clasificacion_laliga"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }
    start_urls = [
        "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
    ]

    def clear_database(self):
        connection = psycopg2.connect(
            database="reto_deportes",
            user="ji156",
            password="admin",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        # Especifica las tablas que deseas eliminar (ajusta según tus necesidades)
        tables_to_clear = ["clasificacion_laliga"]

        for table in tables_to_clear:
            delete_query = f"DELETE FROM {table}"
            cursor.execute(delete_query)

        connection.commit()

        cursor.close()
        connection.close()

    def parse(self, response):
        # Antes de iniciar el scraping, borra los datos existentes en la base de datos
        self.clear_database()

        for equipo in response.css("tbody tr"):
            item = {}
            item["escudo_url"] = equipo.css(
                "img.ue-c-table-ranking__img::attr(src)").get()
            item["nombre_equipo"] = equipo.css(
                "span.nombre-equipo::text").get()
            item["posicion"] = equipo.css("span.pos::text").get()
            item["Puntos"] = equipo.css("td:nth-child(2)::text").get()
            item["PJ"] = equipo.css("td:nth-child(3)::text").get()
            item["PG"] = equipo.css("td:nth-child(4)::text").get()
            item["PE"] = equipo.css("td:nth-child(5)::text").get()
            item["PP"] = equipo.css("td:nth-child(6)::text").get()
            item["GF"] = equipo.css("td:nth-child(7)::text").get()
            item["GC"] = equipo.css("td:nth-child(8)::text").get()

            # Verificar y completar campos requeridos
            if item["nombre_equipo"] is not None:
                item["nombre_equipo"] = item["nombre_equipo"].strip()
            else:
                item["nombre_equipo"] = "Desconocido"

            if item["posicion"] is None:
                item["posicion"] = "Sin posición"

            if item["Puntos"] is None:
                item["Puntos"] = "0"

            if item["PJ"] is None:
                item["PJ"] = "0"

            if item["PG"] is None:
                item["PG"] = "0"

            if item["PE"] is None:
                item["PE"] = "0"

            if item["PP"] is None:
                item["PP"] = "0"

            if item["GF"] is None:
                item["GF"] = "0"

            if item["GC"] is None:
                item["GC"] = "0"

            # Enviar los datos a la base de datos
            self.save_to_database(item)

    def save_to_database(self, item):
        api_url = "http://localhost:8000/clasificacion/api/clasificacion/"

        # Añade la URL del escudo al diccionario 'item'
        item["escudo_url"] = item.get("escudo_url", "")

        # Enviar una solicitud POST con los datos
        response = requests.post(api_url, json=item)

        if response.status_code == 201:
            self.logger.info("Registro creado con éxito")
        else:
            self.logger.error("Error al crear el registro: %s" % response.text)
