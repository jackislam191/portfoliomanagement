from django.db import models

# Create your models here.
from datetime import datetime
# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length= 200)
    money = models.IntegerField()

    def __str__(self):
        return self.name

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=20)
    account_password = models.CharField(max_length=20)


    def __str__(self):
        account_sig = self.account_name + '_' + str(self.account_id)
        return account_sig

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True, default=13)
    stock_name = models.CharField(max_length=50)
    stock_symbol = models.CharField(max_length=20)
    shares = models.DecimalField(max_digits=10, decimal_places =0)
    date = models.DateTimeField(default=datetime.now)
    value = models.DecimalField(max_digits=5, decimal_places =2)

    def __str__(self):
        stock_sig = self.stock_name + '_' + str(self.stock_id)
        return stock_sig
    
