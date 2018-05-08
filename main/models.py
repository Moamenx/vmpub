from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, max_length=50)
    photo = models.FileField(null=False, upload_to=settings.MEDIA_ROOT+'/categories/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=2000)
    short_description = models.CharField(null=False, max_length=70)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    photo = models.FileField(null=False, upload_to=settings.MEDIA_ROOT+'/products/')

    def __str__(self):
        return self.name


class Impression(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=2000)
    photo = models.FileField(null=False, upload_to=settings.MEDIA_ROOT + '/impression/')

    def __str__(self):
        return self.title


class Catalog(models.Model):
    description = models.CharField(null=False, max_length=2000)
    link = models.CharField(null=False, max_length=200)
    photo = models.FileField(null=False, upload_to=settings.MEDIA_ROOT + '/catalog/')

    def __str__(self):
        return self.description[:30]


class ProductPhoto(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, related_name='images')
    photo = models.FileField(null=False, upload_to=settings.MEDIA_ROOT + '/product-photos/')

    def __str__(self):
        return self.product.name

class HotNew(models.Model):
    news = models.CharField(null= False, max_length=150)

    def __str__(self):
        return self.news[:25]
