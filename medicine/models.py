from email.policy import default
from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length =30)
    bio = models.TextField(max_length =300)
    email = models.EmailField()
    phone_number  = models.IntegerField(max_length =30)
    profile_pic = models.ImageField(upload_to = 'articles/')
    category = models.CharField(max_length =30, default="donor")


class Buyer(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number  = models.IntegerField(max_length =30)
    profile_pic = models.ImageField(upload_to = 'articles/')
    category = models.CharField(max_length =30, default="buyer")

class Supplier(models.Model):
    name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    bio = models.TextField(max_length =300)
    email = models.EmailField()
    phone_number  = models.IntegerField(max_length =30)
    profile_pic = models.ImageField(upload_to = 'articles/')
    category = models.CharField(max_length =30, default="supplier")
