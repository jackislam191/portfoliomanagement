from django.test import TestCase
from stock.models import  Stock

class TestAppModels(TestCase):

    def test_model_str(self):
        ticker = Stock.objects.create(ticker="AAPL")
        self.assertEqual(str(ticker), "AAPL")