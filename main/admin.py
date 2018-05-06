from django.contrib import admin
from django.contrib.admin import AdminSite


from main.models import Product, Category, HotNew, ProductPhoto, Impression, Catalog



class InlineProductPhotos(admin.TabularInline):
    model = ProductPhoto

class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductPhotos]
    list_per_page = 20


admin.site.site_header = "VMPUB Control Panel"
admin.site.site_title = "VMPUB Administration"
admin.site.index_title = "VMPUB Administration"
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(HotNew)
admin.site.register(Impression)
admin.site.register(Catalog)


