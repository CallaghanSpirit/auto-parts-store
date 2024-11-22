from django.db import models
from django_extensions.db.fields import AutoSlugField
from transliterate import slugify
from django.urls import reverse

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from = 'name')
    desc = models.TextField(blank=True)
    cats = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    
    def slugify_function(self,content):
        return slugify(content)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('card-page', kwargs={'gd_slug': self.slug})