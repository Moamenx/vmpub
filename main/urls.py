from main.views import *
from django.conf.urls import url, include
from django.contrib import admin
app_name = 'main'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'about-us/', AboutView.as_view(), name='about'),
    url(r'contact-us/', ContactUsView.as_view(), name='contact'),
    url(r'^categories/(?P<cat_name>[\w|\W]+)/', CategoryView.as_view(), name='categories'),
    url(r'^products/(?P<cat_name>[\w|\W]+)/(?P<product_name>[\w|\W]+)', ProductView.as_view(), name='products'),

]
