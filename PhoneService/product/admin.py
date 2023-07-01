from django.contrib import admin
from .models import ProductService, Product, ProductGuarantee, ServiceDiscount, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductGuarantee)
admin.site.register(ProductService)
admin.site.register(ServiceDiscount)
