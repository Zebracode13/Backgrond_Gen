from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    company_email = models.EmailField()
    message = models.DateField()
    phone = models.IntegerField()




