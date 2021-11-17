import collections
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import OrderedDict

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_html_template():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template("template.html")

    return template


def get_beverages_table():
    beverages = pandas.read_excel(
        'wine.xlsx',
        sheet_name='Лист1',
        usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
        na_values=' ',
        keep_default_na=False
        )
    beverages_dict = (beverages.to_dict(orient='records'))

    return beverages_dict


def get_assortment(beverages_dict):
    assortment = collections.defaultdict(list)
    for beverages in beverages_dict:
        assortment[beverages['Категория']].append(beverages)
    assortment = OrderedDict(sorted(assortment.items()))

    return assortment


def get_rendered_page(assortment, template):
    rendered_page = template.render(
        year=date.today().year,
        assortment=assortment
            )

    return rendered_page


def write_rendered_page(rendered_page):
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    template = get_html_template()
    beverages_dict = get_beverages_table()
    assortment = get_assortment(beverages_dict)
    rendered_page = get_rendered_page(assortment, template)
    write_rendered_page(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
