from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_number = models.CharField(max_length=20)
