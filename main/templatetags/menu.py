from django import template
from main.models import Category
register = template.Library()

@register.filter(name='showmenu')
def show_menu():
    cat_names = []
    categories = Category.objects.all()
    for category in categories:
        cat_names.append(category.name)
    return {'cats': cat_names}
