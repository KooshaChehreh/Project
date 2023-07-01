from django import forms
from .models import Product
from order.models import Station


class AddToCartForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddToCartForm, self).__init__(*args, **kwargs)
        try:
            prod_list = Product.objects.filter(user__username=self.request.user)
            station_list = Station.objects.all()
            self.CHOICES = []
            self.station = []
            for product in prod_list:
                self.CHOICES.append((f'{product.brand}', f'{product.brand}'))
            for station in station_list:
                self.station.append((f'{station.name}', f'{station.name}'))
            self.fields['product'].choices = tuple(self.CHOICES)
            self.fields['station'].choices = tuple(self.station)
        except AttributeError:
            pass

    product = forms.ChoiceField(choices=(), label='Device')
    station = forms.ChoiceField(choices=(), label='Station')
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'qty'}))


class ProductForm(forms.Form):
    imei1 = forms.IntegerField(label='IMEI1', widget=forms.TextInput(attrs={'placeholder': 'IMEI1'}))
    brand = forms.CharField(max_length=100, label='Brand', widget=forms.TextInput(attrs={'placeholder': 'Brand'}))
    model = forms.CharField(max_length=100, label='Model', widget=forms.TextInput(attrs={'placeholder': 'Model'}))
