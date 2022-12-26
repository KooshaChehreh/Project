from django.shortcuts import render
from django.views import View
from .models import Order, OrderItems
from django.contrib.auth.decorators import login_required


class OrderItemView(View):
    def get(self, request, *args, **kwargs):
        items = request.session['cart']
        for item in items:
            an_item = OrderItems(

            )
