from django.urls import path
from .views import OrderItemView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('order_items/', login_required(OrderItemView.as_view()), name='order_items'),
]

