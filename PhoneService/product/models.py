from django.db import models

from django.db import models
from django.contrib.auth.models import models
from PhoneService.core.models import BaseModel
from PhoneService.user.models import User


class Product(BaseModel):
    brand = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    guarantee_code = models.BigIntegerField(null=False, blank=False)
    guarantee_start_date = models.DateTimeField(auto_now_add=True)
    guarantee_end_date = models.DateTimeField()
    image = models.ImageField(upload_to='/products')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} ({self.model})'


class ProductGuarantee(BaseModel):
    guarantee_code = models.BigIntegerField(primary_key=True)
    guarantee_duration = models.DateTimeField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guarantee_code}'


class ProductService(BaseModel):
    service_name = models.CharField(max_length=100)
    price = models.BigIntegerField(null=False, blank=False)
    description = models.TextField()
    guarantee_support = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f'{self.service_name}'


class ServiceDiscount(BaseModel):
    name = models.CharField(max_length=200)
    percent = models.IntegerField(blank=True)
    amount = models.IntegerField()
    description = models.TextField()
    service = models.ForeignKey(ProductService, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

