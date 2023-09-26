from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
# Create your tests here.

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-09-25', 'customer_name': 'Gaurav_Test1'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.url = reverse('invoice-list')

    def test_create_invoice(self):
        response = self.client.post(self.url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)