from django.contrib import admin
from django.urls import path
from .views import CategoryListView, MobileServiceListView, TabletServiceListView, \
    LaptopServiceListView, ServiceDetailView

urlpatterns = [
    path('', CategoryListView.as_view(template_name='categories.html'), name='category'),
    path('Mobile/', MobileServiceListView.as_view(), name='mobile_services'),
    path('Laptop/', LaptopServiceListView.as_view(), name='laptop_services'),
    path('Tablet/', TabletServiceListView.as_view(), name='tablet_services'),
    path('service_datail/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
]
