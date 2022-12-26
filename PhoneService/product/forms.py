from django import forms
from .models import Product


class AddToCartForm(forms.Form):

    """kwargs.pop removes the key and returns the value if exists!"""

    product = forms.ChoiceField(label='Device', choices=(('S', 'Small'), ('M', "Medium")))
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'qty'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddToCartForm, self).__init__(*args, **kwargs)
        try:
            prod_list = Product.objects.filter(user__username=self.user.username)
            self.CHOICES = []
            for product in prod_list:
                self.CHOICES.append((f'{product.brand}', f'{product.brand}'))
            self.fields['product'].choices = (('S', 'Small'), ('M', "Medium"))
            print(tuple(self.CHOICES))
        except AttributeError:
            pass


class ProductForm(forms.Form):
    imei1 = forms.IntegerField(label='IMEI1', widget=forms.TextInput(attrs={'placeholder': 'IMEI1'}))
    brand = forms.CharField(max_length=100, label='Brand', widget=forms.TextInput(attrs={'placeholder': 'Brand'}))
    model = forms.CharField(max_length=100, label='Model', widget=forms.TextInput(attrs={'placeholder': 'Model'}))
