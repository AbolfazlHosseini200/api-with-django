from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    number = models.CharField(max_length=11)
    password = models.CharField(max_length=4)


class InsuranceUsers(models.Model):
    user = User()
    number = models.CharField(max_length=11)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=50)
    bmi = models.CharField(max_length=4)
    smoke = models.BooleanField()
