from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

class Account(models.Model):
    user = models.ForeignKey('auth.User', models.CASCADE)
    account = models.TextField()

    def __str__(self):
        return self.user.get_username()

class Obligation(models.Model):
    user = models.ForeignKey('auth.User', models.CASCADE)
    bill = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    rent = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.user.get_username()

class Supplier(models.Model):
    name = models.TextField()
    title = models.TextField()
    account = models.TextField()

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    quantity = models.IntegerField()
    receipt = models.ImageField()
    user = models.ForeignKey('auth.User', models.CASCADE)
    
    def __str__(self):
        return self.name

class Bill(models.Model):
    company = models.ForeignKey('Supplier', models.CASCADE)
    title = models.TextField()
    value = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    date = models.DateField()
    paid = models.BooleanField()

    def __str__(self):
        return self.company.name + " " + str(self.value)

class Income(models.Model):
    sid = models.IntegerField()
    title = models.TextField()
    user = models.ForeignKey('auth.User', models.CASCADE)
    date = models.DateTimeField()
    value = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')

    def __str__(self):
        return self.user.get_username() + " " + str(self.value)
