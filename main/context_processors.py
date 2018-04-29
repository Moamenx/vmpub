from main.models import Category


def get_category_menu(request):
    cat_names = []
    categories = Category.objects.all()
    for category in categories:
        cat_names.append(category.name)
    return {
        'categories': cat_names,
    }
