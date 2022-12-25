from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'qty'}))

