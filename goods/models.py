from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=255)
    cats = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]