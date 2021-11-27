import json

from django.shortcuts import render
from datetime import datetime

from django.conf import settings

from mainapp.models import Product, ProductCategory


def index(request):
    products_list = Product.objects.all()[:4]

    context = {
        'title': 'магазин',
        'date': datetime.now(),
        'products': products_list,
    }
    return render(request, 'mainapp/index.html', context)

#
# links_menu = [
#     {'link_name': 'home', 'name': 'Дом'},
#     {'link_name': 'modern', 'name': 'Модерн'},
#     {'link_name': 'office', 'name': 'Офис'},
#     {'link_name': 'classic', 'name': 'Классика'},
# ]


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
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
