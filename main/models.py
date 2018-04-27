from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, max_length=50)
    photo = models.FileField(null=False, upload_to='main/static/main/images/categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=2000)
    short_description = models.CharField(null=False, max_length=70)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name


class HotNew(models.Model):
    news = models.CharField(null= False, max_length=150)

    def __str__(self):
        return self.news[:25]
