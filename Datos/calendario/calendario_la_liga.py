from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import psycopg2
import requests


class LaLiga(Item):
    local = Field()
    visitante = Field()
    resultado = Field()
    jornada = Field()


class CalendarioCrawler(CrawlSpider):
    name = 'calendario_laliga'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }
    allowed_domains = ['marca.com']
    download_delay = 1
    start_urls = ['https://www.marca.com/futbol/']

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/futbol/primera-division/calendario\.html'
            ), follow=True, callback='parse_laliga'
        ),
    )

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
        tables_to_clear = ["calendario_laliga"]

        for table in tables_to_clear:
            delete_query = f"DELETE FROM {table}"
            cursor.execute(delete_query)

        connection.commit()

        cursor.close()
        connection.close()

    def parse_laliga(self, response):
        self.clear_database()  # Borra los datos existentes en la base de datos

        for match in response.xpath('//table[@class="jor agendas"]'):
            # Obtén el texto de la etiqueta <caption> dentro del contexto del bucle
            jornada = match.xpath('caption/text()').get()

            for match_row in match.xpath('.//tbody/tr'):
                item = LaLiga()
                item['local'] = match_row.xpath(
                    './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()').get()
                item['visitante'] = match_row.xpath(
                    './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()').get()

                resultado = match_row.xpath(
                    './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
                fecha = match_row.xpath(
                    './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

                if resultado:
                    item['resultado'] = resultado
                elif fecha:
                    item['resultado'] = fecha
                else:
                    item['resultado'] = ''

                # Asocia la jornada con cada partido
                item['jornada'] = jornada.strip() if jornada else ''
                self.save_to_database(item)

    def save_to_database(self, item):
        # Convert Scrapy item to a dictionary
        item_dict = dict(item)

        # URL de la API de tu base de datos
        api_url = "http://localhost:8000/calendario/api/calendario/laliga/"

        # Enviar una solicitud POST con los datos
        response = requests.post(api_url, json=item_dict)

        if response.status_code == 201:
            self.logger.info("Registro creado con éxito")
        else:
            self.logger.error("Error al crear el registro: %s" % response.text)
