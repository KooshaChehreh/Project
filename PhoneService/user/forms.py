from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Address
from .validators import validate_phone


class UserForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')
    confirm_password = forms.CharField(label='Confirm Password')
    phone = forms.IntegerField()

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "passwords does not match"
            )
        else:
            return True


class OtpForm(forms.Form):
    otp_code = forms.IntegerField(label='Enter your code please', required=True)


class ProfileForm(forms.Form):
    phone = forms.IntegerField(validators=['validate_phone', ], required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField()


class AddressForm(forms.Form):
    city = forms.CharField()
    district = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True, )
