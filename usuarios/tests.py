from django.test import TestCase
from django.urls import resolve, reverse


class UsuariosUrlsTest(TestCase):
    def test_home_url_resolves(self):
        self.assertEqual(resolve('/usuarios/').view_name, 'home')

    def test_password_reset_url_exists(self):
        self.assertEqual(reverse('password_reset'), '/usuarios/password-reset/')
