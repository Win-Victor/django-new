from django.core.management import BaseCommand
from django.db.models import Q
from mainapp.models import Product, ProductCategory


class Command(BaseCommand):

    def handle(self, *args, **options):
        # product_list = Product.objects.filter(Q(category__name='дом') | Q(category__name='офис'))
        product_list = Product.objects.filter(category__name__in=['дом', 'офис'])

        print(product_list)
