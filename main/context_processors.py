from main.models import Category,Impression,Catalog


def get_category_menu(request):
    cat_names = []
    categories = Category.objects.all()
    for category in categories:
        cat_names.append(category.name)

    return {
        'categories': cat_names,
        'impressions': Impression.objects.all(),
        'catalogs': Catalog.objects.all(),
    }
