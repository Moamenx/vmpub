from main.views import *
from django.conf.urls import url, include
from django.contrib import admin
app_name = 'main'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
     url(r'impression/', ImpressionView.as_view(), name='impression'),
    url(r'catalog/', CatalogView.as_view(), name='catalog'),
    url(r'details/', DetailsView.as_view(), name='details'),
    url(r'contact-us/', ContactUsView.as_view(), name='contact'),
    url(r'^categories/(?P<cat_name>[\w|\W]+)/', CategoryView.as_view(), name='categories'),
    url(r'^products/(?P<cat_name>[\w|\W]+)/(?P<product_name>[\w|\W]+)/', ProductView.as_view(), name='products'),

]

import os
import main.models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def update_database():
    for photo in Category.objects.all():
        name = photo.photo.name.split("/categories/")[1]
        final = BASE_DIR + '/media/categories/' + name
        photo.photo = final
        photo.save()
    for photo in Product.objects.all():
        name = photo.photo.name.split("/products/")[1]
        final = BASE_DIR + '/media/products/' + name
        photo.photo = final
        photo.save()
    for photo in ProductPhoto.objects.all():
        name = photo.photo.name.split("/product-photos/")[1]
        final = BASE_DIR + '/media/product-photos/' + name
        photo.photo = final
        photo.save()

update_database()
