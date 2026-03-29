from http import HTTPStatus

from django.test import TestCase

from .forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):
    def test_get(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, '<h1>Register</h1>', html=True)

    def test_post_success(self):
        response = self.client.post(
            '/register/',
            data={
                'username': 'test',
                'password': 'test',
                'phone_number': '+000000000000',
                'first_name': 'Test',
                'last_name': 'Test',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_form(self):
        form = CustomUserCreationForm(
            data={
                'username': 'test',
                'password': 'test',
                'phone_number': '+000000000000',
                'first_name': 'Test',
                'last_name': 'Test',
            },
        )
        self.assertEqual(form.data['username'], 'test')
