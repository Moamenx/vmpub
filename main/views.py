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
        context = {'news': get_news(), 'cats': Category.objects.all(), 'slide': SlideShow.objects.all()}
        return render(request, 'main/indeex.html', context)

    def post(self, request):
        pass

class SearchView(View):
    template_name = 'main/search.html'


    def post(self, request):
        msg = request.POST.get('filter')
        if msg == "":
            context = {'news': get_news(), 'cats': Category.objects.all(), 'result': None}
            return render(request, 'main/search.html', context)
        product_result = []
        category_result = []
        filtered_msg = msg.lower()
        for p in Product.objects.all():
            if p.name.lower().__contains__(filtered_msg) or p.description.lower().__contains__(filtered_msg):
                product_result.append(p)
        for cat in Category.objects.all():
            if cat.name.replace(' ','').lower().__contains__(filtered_msg):
                category_result.append(cat)
        for cat in category_result:
            print(cat.name)
        for p in product_result:
            print(p.name)
        context = {'news': get_news(), 'cats': Category.objects.all(), 'msg': msg, 'result':product_result}
        return render(request, 'main/search.html', context)


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
        subject = self.request.POST.get('subject')
        name = self.request.POST.get('name')
        print(message)
        # if name and message and phone!= "":
        send_mail("VMPUB - "+ subject,
                  "Name: " + name + "\n" + "Contact Email: " + email + "\n" + "\n" + "Message: " + message,
                  settings.EMAIL_HOST_USER, ['isiskheresto@hotmail.com'], fail_silently=False)
        messages.success(request, 'Thank you for sending us an email!')
        return render(request, 'main/contact.html')


class CategoryView(View):
    template_name = 'main/category.html'

    def get(self, request, cat_name):
        product_photos = None
        products = Product.objects.all()
        catName = cat_name
        if '-' in catName:
            catName = cat_name.replace('-', ' ')
        try:
            category = Category.objects.get(name=catName)
        except Category.DoesNotExist:
            category = None
        try:
            products = Product.objects.all().filter(category=category)
           #product_photos = ProductPhoto.objects.all()
        except Product.DoesNotExist:
            products = None
            product_photos = None

        context = {'category_name': catName, 'product_photos': product_photos, 'products': products,
                   'cats': Category.objects.all()}
        return render(request, 'main/category.html', context)


class ProductView(View):
    template_name = 'main/product.html'

    def get(self, request, cat_name, product_name):
        context = {}
        productName = product_name
        if '-' in productName:
           productName = product_name.replace('-', ' ')
        if Product.objects.all().filter(name=productName).exists():
            try:
                product = Product.objects.get(name=productName)
                product_photos = ProductPhoto.objects.all().filter(product=product)
            except (Product.DoesNotExist, ProductPhoto.DoesNotExist):
                product_photos = None
                product = None
            context = {'product': product, 'category': cat_name, 'product_photos': product_photos}

        return render(request, 'main/product.html', context)
