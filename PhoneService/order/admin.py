from django.contrib import admin
from .models import Station, Order, OrderItems, ReceiptDiscount, Receipt

admin.site.register(Station)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ReceiptDiscount)
admin.site.register(Receipt)

