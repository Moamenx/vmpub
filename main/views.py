from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
import re
from django.conf import settings


# Create your views here.
def get_news():
    news = []
    hot_news = HotNew.objects.all()
    if hot_news:
        for n in hot_news:
            news.append(n.news)
    return news


def get_categories():
    cat_names = []
    categories = Category.objects.all()
    for category in categories:
        cat_names.append(category.name)
    categories_names = []
    for name in cat_names:
        categories_names.append(re.sub('\s+', '-', name))
    return categories_names


def get_cats():
    cats = Category.objects.all()


class HomeView(View):
    template_name = 'main/indeex.html'

    def get(self, request):
        context = {'news': get_news(), 'cats': Category.objects.all()}
        return render(request, 'main/indeex.html', context)

    def post(self, request):
        pass


class AboutView(View):
    template_name = 'main/about.html'

    def get(self, request):
        return render(request, 'main/about.html')


class DetailsView(View):
    template_name = 'main/details.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/details.html', context)


class ImpressionView(View):
    template_name = 'main/impression.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/impression.html', context)


class CatalogView(View):
    template_name = 'main/catalog.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/catalog.html', context)


class ContactUsView(View):
    template_name = 'main/contact.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/contact.html', context)

    def post(self, request):
        email = self.request.POST.get('email')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            context = {'categories': get_categories(), 'msg': 'Invalid email address'}
            return render(request, 'main/contact.html', context)
        message = self.request.POST.get('message')
        name = self.request.POST.get('name')
        print(message)
        # if name and message and phone!= "":
        send_mail("Business Request",
                  "Name: " + name + "\n" + "Contact Email: " + email + "\n" + "\n" + "Message: " + message,
                  settings.EMAIL_HOST_USER, ['20140165@fa-hists.edu.eg'], fail_silently=False)
        messages.success(request, 'Thank you for sending us an email!')
        return render(request, 'main/contact.html')


class CategoryView(View):
    template_name = 'main/category.html'

    def get(self, request, cat_name):
        product_photos = None
        products = Product.objects.all()
        try:
            category = Category.objects.all().filter(name=cat_name)
        except Category.DoesNotExist:
            category = None
        try:
            products = Product.objects.all().filter(category=category)
          # product_photos = ProductPhoto.objects.all()
        except Product.DoesNotExist:
            products = None
            product_photos = None

        context = {'category_name': cat_name, 'product_photos': product_photos, 'products': products,
                   'cats': Category.objects.all()}
        return render(request, 'main/category.html', context)


class ProductView(View):
    template_name = 'main/product.html'

    def get(self, request, cat_name, product_name):
        context = {}
        product_photos = None
        if Product.objects.all().filter(name=product_name).exists():
            try:
                product = Product.objects.get(name=product_name)
                #product_photos = ProductPhoto.objects.all().filter(product=product)
            except (Product.DoesNotExist, ProductPhoto.DoesNotExist):
                product_photos = None
                product = None
            context = {'product': product, 'category': cat_name, 'product_photos': product_photos}

        return render(request, 'main/product.html', context)
