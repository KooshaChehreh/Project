from django.db import models


from django.db import models
from django.contrib.auth.models import models
from core.models import BaseModel
from user.models import User
from product.models import ProductService, Product


class Station(BaseModel):
    name = models.CharField(max_length=200)
    boss = models.CharField(max_length=200)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return f'{self.name} station!'


class Order(BaseModel):
    STATUS = [('A', 'Accepted'), ('W', 'Waiting'), ('R', 'Rejected')]
    status = models.CharField(max_length=1, choices=STATUS, default='W')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}{self.status}-{self.station.name}'


class OrderItems(BaseModel):
    service = models.ForeignKey(ProductService, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class ReceiptDiscount(BaseModel):
    name = models.CharField(max_length=100)
    percent = models.IntegerField(null=True, default=0)
    amount = models.IntegerField(default=0)
    is_paid = models.BooleanField()

    def __str__(self):
        return self.name


class Receipt(BaseModel):
    total_price = models.IntegerField()
    receipt_discount = models.ForeignKey(ReceiptDiscount, on_delete=models.CASCADE)
