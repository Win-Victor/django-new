import json

from django.shortcuts import render
from datetime import datetime

from django.conf import settings


def index(request):
    context = {
        'title': 'магазин',
        'date': datetime.now(),
    }
    return render(request, 'mainapp/index.html', context)


links_menu = [
    {'href': 'products', 'name': 'Все'},
    {'href': 'products_home', 'name': 'Дом'},
    {'href': 'products_modern', 'name': 'Модерн'},
    {'href': 'products_office', 'name': 'Офис'},
    {'href': 'products_classic', 'name': 'Классика'},
]


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'товары',
    }
    return render(request, 'mainapp/products.html', context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'товары',
    }
    return render(request, 'mainapp/products.html', context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'товары',
    }
    return render(request, 'mainapp/products.html', context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'товары',
    }
    return render(request, 'mainapp/products.html', context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'товары',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    # context = {'title': 'контакты',}
    with open(f'{settings.BASE_DIR}/contacts.json') as contacts_file:
        context = {
            'contacts': json.load(contacts_file)
        }
    context['title'] = 'контакты'
    return render(request, 'mainapp/contact.html', context)
