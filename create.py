import requests
from bs4 import BeautifulSoup
import re


class ParsingNews:

    def __init__(self, url, tags):
        self.url = url
        self.tags = tags
        self.info = []

    def newsLoading(self):
        """Создание списка элементов с новостями"""
        print('Загружается страница {}...'.format(self.url))
        res = requests.get(self.url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, features="html.parser")
        catalogElem = soup.select(self.tags)
        return catalogElem

    def newsContent(self, catalogElem):
        """Создание списка новостей"""
        print('Перебор элементов...')
        for i in catalogElem:
            title = i.getText().split()
            title = ' '.join(title)
            self.info.append(title)
        return self.info

    def singleNews(self, info):
        """Создание списка новостей построчно"""
        news = ' - ' + ' \n - '.join(info)
        return news

    
    def singleCurs(self, info):
        """Создание курса валют построчно ЦБ"""
        regex = re.compile(r'(.{39})(.{11})(.{9})(.{9})(.{5})(.{9})(.*)')
        mo = regex.search(info[0])
        act, dollar, priceDollarYesterday, priceDollar, euro, priceEuroYesterday, priceEuro = mo.groups()
        info[0] = (dollar + ':' + priceDollar + '\n ' + euro + ':' + priceEuro)
        news = ' - '.join(info)
        return news


def content():
    """Запуск парсера новостей ТАСС"""
    url = 'https://tass.ru/rasprostranenie-koronavirusa-novogo-tipa'
    tags = 'div.themeCard_title__3Fm_V span'
    Pars = ParsingNews(url, tags)
    catalogElem = Pars.newsLoading()
    info = Pars.newsContent(catalogElem)
    news = Pars.singleNews(info)
    # print('Создание списка новостей закончено...')
    return news

def curs():
    """Запуск парсера курса доллара и евро на сайте ЦБ РФ"""
    url = 'https://www.cbr.ru/'
    tags = 'tbody'
    pars = ParsingNews(url, tags)
    catalogElem = pars.newsLoading()
    info = pars.newsContent(catalogElem)
    news = pars.singleCurs(info)
    return news

