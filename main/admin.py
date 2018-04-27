from django.contrib import admin


from main.models import Product, Category, HotNew


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(HotNew)

