from django.test import TestCase
from django.urls import reverse
from django.shortcuts import redirect
from http import HTTPStatus
from django.contrib.auth import get_user_model


# Create your tests here.
class RegisterUserTestCase(TestCase):
    def setUp(self):
        "Инициализация перед выполнением каждого теста"
        return super().setUp()
    # def test_form_register(self):
    #     path = reverse('users:register')
    #     response = self.client.get(path)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        data = {
            'username':'Alan',
            'email': 'tsoloevalanoid@gmail.com',
            'first_name': 'Сергей',
            'last_name':'Гей',
            'password':'Mikado2006',
            'password2':'Mikado2006',

        }
        user_model = get_user_model()

        path = reverse('users:register')
        response = self.client.post(path, data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(user_model.objects.get(usename=data['username']))

    def tearDown(self):
        "Действия после выполнения каждого теста"
        return super().tearDown()