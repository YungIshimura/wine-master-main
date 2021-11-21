import collections
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import OrderedDict
import argparse

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def configure_parser():
    parser = argparse.ArgumentParser('''
    Код для сайта Новое русское вино.
    Для запуска необходим Excel файл с данными о вине
    (категория, название, сорт, цена, картинка, акция).
    Вы можете создать свой, либо использовать  дефолтный файл wine.xlsx,
    который находится в корне проекта.
    ''')
    parser.add_argument(
        '--path',
        default='wine.xlsx',
        help=('Введите название Excel файла'))

    return parser


def get_html_template():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    return template


def get_beverages():
    beverages = pandas.read_excel(
        args.path,
        sheet_name='Лист1',
        usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
        na_values=' ',
        keep_default_na=False
        )
    beverages = beverages.to_dict(orient='records')

    return beverages


def get_assortment(beverages):
    assortment = collections.defaultdict(list)
    for beverage in beverages:
        assortment[beverage['Категория']].append(beverage)
    assortment = OrderedDict(sorted(assortment.items()))

    return assortment


def get_wineary_age():
    age = date.today().year - year_winery_founded
    if age % 10 == 1:
        wineary_age = f'Уже {age} год с вами! '
    elif age % 10 == 2 or 3 or 4:
        wineary_age = f'Уже {age} года с вами! '
    else:
        wineary_age = f'Уже {age} лет с вами! '

    return wineary_age


if __name__ == '__main__':
    year_winery_founded = 1920
    parser = configure_parser()
    args = parser.parse_args()
    template = get_html_template()
    beverages = get_beverages()
    assortment = get_assortment(beverages)
    wineary_age = get_wineary_age()

    rendered_page = template.render(
        wineary_age=wineary_age,
        assortment=assortment
            )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
