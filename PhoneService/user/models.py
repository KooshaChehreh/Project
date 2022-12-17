from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from .validators import validate_phone


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(BaseModel):
    phone = models.CharField(max_length=14, unique=True, null=False, blank=False, validators=[validate_phone, ])
    email = models.EmailField(unique=True, null=False, blank=False)
    image = models.ImageField(null=True, upload_to='profile/%Y/%m/%d')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Address(BaseModel):
    latitude = models.IntegerField(null=False, blank=False)
    longitude = models.IntegerField(null=False, blank=False)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')

    class Meta:
        verbose_name_plural = 'Addresses'


