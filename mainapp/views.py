import json

from django.shortcuts import render, get_object_or_404
from datetime import datetime

from django.conf import settings

from basketapp.models import Basket
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

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'Все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        context = {
            'links_menu': links_menu,
            'title': 'товары',
            'products': products_list,
            'category': category_item,
            'basket': sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True))),
        }
        return render(request, 'mainapp/products_list.html', context)


    context = {
        'links_menu': links_menu,
        'title': 'товары',
        'hot_product': Product.objects.all().first(),
        'same_products': Product.objects.all()[3:5],
        'basket': sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True))),

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
