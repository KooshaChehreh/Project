from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'qty'}))


class ProductForm(forms.Form):
    imei1 = forms.IntegerField(label='IMEI1', widget=forms.TextInput(attrs={'placeholder': 'IMEI1'}))
    brand = forms.CharField(max_length=100, label='Brand', widget=forms.TextInput(attrs={'placeholder': 'Brand'}))
    model = forms.CharField(max_length=100, label='Model', widget=forms.TextInput(attrs={'placeholder': 'Model'}))

