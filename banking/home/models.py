from email.policy import default
from unicodedata import name
from django.db import models
from django.urls import reverse_lazy


# Create your models here.


class account(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name
class District(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, verbose_name='district', on_delete = models.CASCADE)
    name = models.CharField(max_length = 40)
    def __str__(self):
        return self.name

class form_register(models.Model):
    name = models.CharField(max_length = 100)
    DOB = models.DateField()
    AGE = models.CharField(max_length = 2)
    Gender = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10)
    email_id = models.EmailField()
    adress = models.TextField(max_length = 100)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    account_type = models.ForeignKey(account,on_delete = models.CASCADE)
    debit_card = models.BooleanField( default = False)
    credit_card = models.BooleanField(default = False)
    Cheque_book = models.BooleanField( default = False)