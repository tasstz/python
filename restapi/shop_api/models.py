from django.db import models

class Product(models.Model):

    title = models.CharField('title', max_length=255)
    price = models.FloatField('price', default=0.0)
    description = models.TextField('description', max_length=255, default='no_description')

    class Meta:
        managed = True
        verbose_name = 'Product'
