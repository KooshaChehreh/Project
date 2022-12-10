from django.test import TestCase
from .models import Product, ProductGuarantee, ProductService, ServiceDiscount


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(imei1=1234567891230, brand="iphone", model='13')
        Product.objects.create(imei1=1234567891123, brand="iphone", model='11')

    def test_product_image(self):
        """whether product contains image or not correctly identified"""
        prod1 = Product.objects.get(imei1=1234567891230)
        prod2 = Product.objects.get(imei1=1234567891123)
        self.assertEqual(prod1.image.name, '')
        self.assertEqual(prod2.image.name, '')

    def test_product_creation(self):
        prod1 = Product.objects.get(imei1=1234567891230)
        if prod1 is not None:
            test_value = True
            self.assertTrue(test_value, 'Product was created!')

    def test_brand_max_length(self):
        prod1 = Product.objects.get(imei1="1234567891230")
        max_length = prod1._meta.get_field('brand').max_length
        self.assertEqual(max_length, 100)


class ProductGuaranteeTestCase(TestCase):

    def setUp(self):
        Product.objects.create(imei1=1234567891230, brand="iphone", model='13')
        Product.objects.create(imei1=1234567891123, brand="iphone", model='11')
        ProductGuarantee.objects.create(guarantee_code=1234567123, product=Product.objects.get(imei1=1234567891230))
        ProductGuarantee.objects.create(guarantee_code=9876543123, product=Product.objects.get(imei1=1234567891123))

    def test_product_guarantee_code_length(self):
        prod_guarantee_1 = ProductGuarantee.objects.get(guarantee_code=1234567123)
        prod_guarantee_2 = ProductGuarantee.objects.get(guarantee_code=1234567123)
        self.assertEqual(len(str(prod_guarantee_1.guarantee_code)), 10)
        self.assertEqual(len(str(prod_guarantee_2.guarantee_code)), 10)
