from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def clean(self):
        self.ticker = self.ticker.upper()

    def __str__(self):
        return self.ticker
    