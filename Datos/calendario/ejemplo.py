from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import psycopg2
import requests


class BaseItem(Item):
    local = Field()
    visitante = Field()
    resultado = Field()


class LaLiga(BaseItem):
    pass


class Premier(BaseItem):
    pass


class Bundesliga(BaseItem):
    pass


class SerieA(BaseItem):
    pass


class Ligue1(BaseItem):
    pass


class CalendarioCrawler(CrawlSpider):
    name = 'calendario_laliga'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }
    allowed_domains = ['marca.com']
    download_delay = 1
    start_urls = ['https://www.marca.com/futbol/']

    rules = (
        # LaLiga
        Rule(
            LinkExtractor(
                allow=r'/primera-division/calendario\.html'
            ), follow=True, callback='parse_laliga'
        ),
        # Premier
        Rule(
            LinkExtractor(
                allow=r'/premier-league/calendario\.html'
            ), follow=True, callback='parse_premier'
        ),
        # Bundesliga
        Rule(
            LinkExtractor(
                allow=r'/bundesliga/calendario\.html'
            ), follow=True, callback='parse_bundesliga'
        ),
        # SerieA
        Rule(
            LinkExtractor(
                allow=r'/liga-italiana/calendario\.html'
            ), follow=True, callback='parse_seriea'
        ),
        # Ligue1
        Rule(
            LinkExtractor(
                allow=r'/liga-francesa/calendario\.html'
            ), follow=True, callback='parse_ligue1'
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

    def save_to_postgresql(self, item, table_name):
        connection = psycopg2.connect(
            database="reto_deportes",
            user="ji156",
            password="admin",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        insert_query = f"INSERT INTO {table_name} (local, visitante, resultado) VALUES (%s, %s, %s)"
        data = (item["local"], item["visitante"], item["resultado"])
        cursor.execute(insert_query, data)

        connection.commit()

        cursor.close()
        connection.close()

    def parse_laliga(self, response):
        matches = response.xpath('//tbody/tr')

        for match in matches:
            item = ItemLoader(LaLiga(), match)
            item.add_xpath(
                'local', './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()')
            item.add_xpath(
                'visitante', './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()')

            resultado = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
            fecha = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

            if resultado:
                item.add_value('resultado', resultado)
            elif fecha:
                item.add_value('resultado', fecha)
            else:
                item.add_value('resultado', '')

            item = item.load_item()

            # Llama a la función para guardar en PostgreSQL
            self.save_to_postgresql(item, 'laliga_matches')

            yield item

    def parse_premier(self, response):
        matches = response.xpath('//tbody/tr')

        for match in matches:
            item = ItemLoader(Premier(), match)
            item.add_xpath(
                'local', './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()')
            item.add_xpath(
                'visitante', './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()')

            resultado = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
            fecha = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

            if resultado:
                item.add_value('resultado', resultado)
            elif fecha:
                item.add_value('resultado', fecha)
            else:
                item.add_value('resultado', '')

            item = item.load_item()

            # Llama a la función para guardar en PostgreSQL
            self.save_to_postgresql(item, 'premier_matches')

            yield item

    def parse_bundesliga(self, response):
        matches = response.xpath('//tbody/tr')

        for match in matches:
            item = ItemLoader(Bundesliga(), match)
            item.add_xpath(
                'local', './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()')
            item.add_xpath(
                'visitante', './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()')

            resultado = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
            fecha = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

            if resultado:
                item.add_value('resultado', resultado)
            elif fecha:
                item.add_value('resultado', fecha)
            else:
                item.add_value('resultado', '')

            item = item.load_item()

            # Llama a la función para guardar en PostgreSQL
            self.save_to_postgresql(item, 'bundesliga_matches')

            yield item

    def parse_seriea(self, response):
        matches = response.xpath('//tbody/tr')

        for match in matches:
            item = ItemLoader(SerieA(), match)
            item.add_xpath(
                'local', './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()')
            item.add_xpath(
                'visitante', './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()')

            resultado = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
            fecha = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

            if resultado:
                item.add_value('resultado', resultado)
            elif fecha:
                item.add_value('resultado', fecha)
            else:
                item.add_value('resultado', '')

            item = item.load_item()

            # Llama a la función para guardar en PostgreSQL
            self.save_to_postgresql(item, 'seriea_matches')

            yield item

    def parse_ligue1(self, response):
        matches = response.xpath('//tbody/tr')

        for match in matches:
            item = ItemLoader(Ligue1(), match)
            item.add_xpath(
                'local', './/td[@class="local"]//span[contains(@class, "equipo_t")]/text()')
            item.add_xpath(
                'visitante', './/td[@class="visitante"]//span[contains(@class, "equipo_t")]/text()')

            resultado = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "resultado-partido")]/text()').get()
            fecha = match.xpath(
                './/td[@class="resultado"]//span[contains(@class, "fecha")]/text()').get()

            if resultado:
                item.add_value('resultado', resultado)
            elif fecha:
                item.add_value('resultado', fecha)
            else:
                item.add_value('resultado', '')

            item = item.load_item()

            # Llama a la función para guardar en PostgreSQL
            self.save_to_postgresql(item, 'ligue1_matches')

            yield item
