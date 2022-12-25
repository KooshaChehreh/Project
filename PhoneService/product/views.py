from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, ProductService
from .forms import AddToCartForm
from django.shortcuts import get_object_or_404


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


class MobileServiceListView(ListView):
    model = ProductService
    context_object_name = 'mobile_service_list'
    template_name = 'mobiledetail.html'
    queryset = ProductService.objects.filter(category__name='Mobile')


class LaptopServiceListView(ListView):
    model = ProductService
    context_object_name = 'laptop_service_list'
    template_name = 'laptopdetail.html'
    queryset = ProductService.objects.filter(category__name='Laptop')


class TabletServiceListView(ListView):
    model = ProductService
    context_object_name = 'tablet_service_list'
    template_name = 'tabletdetail.html'
    queryset = ProductService.objects.filter(category__name='Tablet')

    def get_context_data(self, **kwargs):
        context = super(TabletServiceListView, self).get_context_data(**kwargs)
        context['temp'] = 'This is just some data to use Get Context'
        return context


class ServiceDetailView(DetailView):
    model = ProductService
    template_name = 'servicedetail.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context['form'] = AddToCartForm()
        context['service'] = get_object_or_404(ProductService, pk=self.kwargs['pk'])
        return context

