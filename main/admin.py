from django.contrib import admin


from main.models import Product, Category, HotNew, ProductPhoto


class InlineProductPhotos(admin.TabularInline):
    model = ProductPhoto

class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductPhotos]
    list_per_page = 20



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(HotNew)

