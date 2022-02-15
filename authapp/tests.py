from django.test import TestCase

from authapp.models import ShopUser


class UserAuthTestCase(TestCase):
    status_code_success = 200
    username = 'django'
    password = 'geekbrains'
    email = 'django@gb.local'

    def setUp(self) -> None:
        self.user = ShopUser.objects.create_superuser(
            username=self.username,
            password=self.password,
            email=self.email
        )

    def test_login_user(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)

    def test_logout_user(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/auth/login/')

        self.assertFalse(response.context['user'].is_anonymous)

        self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/')
        self.assertTrue(response.context['user'].is_anonymous)


class TestUserManagement(TestCase):
    ...

    def test_basket_login_redirect(self):
        # без логина должен переадресовать
        response = self.client.get('/basket/')
        self.assertEqual(response.url, '/auth/login/?next=/basket/')
        self.assertEqual(response.status_code, 302)

        # с логином все должно быть хорошо
        self.client.login(username='tarantino', password='geekbrains')

        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['basket']), [])
        self.assertEqual(response.request['PATH_INFO'], '/basket/')
        self.assertIn('Ваша корзина, Пользователь', response.content.decode())
