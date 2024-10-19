from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.TextField()
    cats = models.IntegerField()