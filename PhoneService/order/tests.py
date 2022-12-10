from django.test import TestCase
from .models import Station, Order, OrderItems, Receipt, ReceiptDiscount, User


class StationTestCase(TestCase):
    def setUp(self):
        Station.objects.create(name='First station', city='Babol', district=6, latitude=123, longitude=456)
        Station.objects.create(name='Second station', city='Tehran', district=7, latitude=456, longitude=123)

    def test_station_creation(self):
        station_1 = Station.objects.get(name='First station')
        self.assertIsInstance(station_1, Station)


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        Station.objects.create(name='First station', city='Babol', district=6, latitude=123, longitude=456)
        User.objects.create(username="koosha", password="Qwerty1234", is_staff=False)
        Order.objects.create(status='W', user=User.objects.get(username="koosha"),
                             station=Station.objects.get(name='First station'))

    def test_order_creation(self):
        # Todo: I got sth by chance :) ! maybe I should expand that to other models.
        order_1 = Order.objects.get(user__username='koosha')
        self.assertIsInstance(order_1, Order)
