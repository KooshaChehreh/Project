from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from PhoneService.core.models import BaseModel


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, related_name='username')
    password = models.CharField()
    is_staff = models.BooleanField()

    def __str__(self):
        return self.username


class Profile(BaseModel):
    phone = models.CharField(unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(BaseModel):
    latitude = models.IntegerField(null=False, blank=False)
    longitude = models.IntegerField(null=False, blank=False)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_plural_name = 'Addresses'


