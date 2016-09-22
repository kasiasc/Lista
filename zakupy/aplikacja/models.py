from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
		
    def __unicode__(self):
          return str(self.name)
		
class List(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=128)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.title
		
    def __unicode__(self):
        return str(self.title)

# Create your models here.
