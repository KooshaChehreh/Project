from django.db import models
from django.db import models
from django.contrib.auth.models import models
from core.models import BaseModel
from user.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Product(BaseModel):
    imei1 = models.BigIntegerField(validators=[MaxLengthValidator(13), MinLengthValidator(13)], unique=True,
                                   primary_key=True, null=False, blank=False)
    brand = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return f'{self.brand} ({self.model})'


class ProductGuarantee(BaseModel):
    guarantee_code = models.BigIntegerField(validators=[MaxLengthValidator(12), MinLengthValidator(12)], null=True, default=0)
    guarantee_duration = models.DateTimeField(null=True)
    guarantee_start_date = models.DateTimeField(null=True)
    guarantee_end_date = models.DateTimeField(null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guarantee_code}'


class ServiceDiscount(BaseModel):
    name = models.CharField(max_length=200)
    percent = models.IntegerField(blank=True)
    amount = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductService(BaseModel):
    service_name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    guarantee_support = models.BooleanField(null=False, blank=False)
    discount = models.OneToOneField(ServiceDiscount, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.service_name}'
