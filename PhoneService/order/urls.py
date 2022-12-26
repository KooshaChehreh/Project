from django.urls import path
from .views import OrderItemView


urlpatterns = [
    path('order_items/', OrderItemView.as_view(), name='order_items'),
]

