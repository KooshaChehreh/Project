from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import User, Profile, Address
from .validators import validate_phone
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group


class UserForm(UserCreationForm):
    phone = forms.CharField(validators=[validate_phone], widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    password1 = forms.CharField(max_length=25, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
        }

    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "passwords does not match"
    #         )
    #     else:
    #         return True


class OtpForm(forms.Form):
    otp_code = forms.IntegerField(required=True)


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


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'phone', 'password',)

