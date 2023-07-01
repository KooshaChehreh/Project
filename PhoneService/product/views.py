import json

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Category, ProductService, Product
from order.models import Order
from .forms import AddToCartForm, ProductForm
from order.models import Station
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


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
        context['form'] = AddToCartForm(request=self.request)
        context['service'] = get_object_or_404(ProductService, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = AddToCartForm(request.POST, request=self.request)
        if form.is_valid():
            q = form['station'].value()
            order = Order(
                user=self.request.user,
                station=Station.objects.get(name=q)
            )
            if 'cart' not in request.session.keys():
                request.session['cart'] = {
                    'service_pk': self.kwargs['pk'],
                    'quantity': form['quantity'].value(),
                    'device': Product.objects.get(brand=form['product'].value()),
                    'station': Station.objects.get(name=form['station'].value()),
                    'order': order
                }
            else:
                request.session['cart'].update({
                    'service_pk': self.kwargs['pk'],
                    'quantity': form['quantity'].value(),
                    'device': form['product'],
                    'station': form['station'],
                    'order': order
                })
        else:
            print(form.errors)
        return redirect('order_items')


class AddUserProduct(View):

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'product.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                imei1=form['imei1'].value(),
                brand=form['brand'].value(),
                model=form['model'].value(),
                user=request.user
            )
            product.save()
        return redirect('product_list')


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'productlist.html'

    def get_queryset(self):
        username = self.request.user.username
        query = Product.objects.filter(user__username=username)
        return query
