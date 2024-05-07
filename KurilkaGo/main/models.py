from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('name' ,max_length=20)