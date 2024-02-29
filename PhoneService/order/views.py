from django.shortcuts import render, redirect
from django.views import View
from .models import Order, OrderItems
from product.models import ProductService, Product


class OrderItemView(View):
    def get(self, request, *args, **kwargs):
        items = request.session['cart']
        for item in items:
            an_item = OrderItems(
                service=ProductService.objects.get(pk=item['service_pk']),
                product=Product.objects.get(imei1=item['device']['imei1']),
                order=request.session['order']
            )
            print(an_item.order.station)
        return redirect('login')
#