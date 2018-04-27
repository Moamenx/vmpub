from main.views import *
from django.conf.urls import url, include
from django.contrib import admin
app_name = 'main'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'about-us/', AboutView.as_view(), name='about'),
     url(r'impression/', ImpressionView.as_view(), name='impression'),
    url(r'catalog/', CatalogView.as_view(), name='catalog'),
    url(r'details/', DetailsView.as_view(), name='details'),
    url(r'contact-us/', ContactUsView.as_view(), name='contact'),
    url(r'^categories/', CategoryView.as_view(), name='categories'),
    url(r'^products/', ProductView.as_view(), name='products'),

]
# (?P<cat_name>[\w|\W]+)/
#(?P<cat_name>[\w|\W]+)/(?P<product_name>[\w|\W]+)