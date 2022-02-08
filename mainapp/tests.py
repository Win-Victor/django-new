from django.test import TestCase
# from django.test.client import Client
from mainapp.models import Product, ProductCategory


class MainappSmokeTest(TestCase):

    def setUp(self) -> None:
        category = ProductCategory.objects.create(
            name='cat1'
        )
        for i in range(10):
            Product.objects.create(
                category=category,
                name=f'prod #{i}',
                description=f'description for prod #{i}'
            )

        # self.client = Client()


    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self) -> None:
        pass
