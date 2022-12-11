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

    def setUp(self) -> None:
        Product.objects.create(imei1=1234567891230, brand="iphone", model='13')
        Product.objects.create(imei1=1234567891123, brand="iphone", model='11')
        ProductGuarantee.objects.create(guarantee_code=1234567123, product=Product.objects.get(imei1=1234567891230))
        ProductGuarantee.objects.create(guarantee_code=9876543123, product=Product.objects.get(imei1=1234567891123))

    def test_product_guarantee_code_length(self):
        prod_guarantee_1 = ProductGuarantee.objects.get(guarantee_code=1234567123)
        prod_guarantee_2 = ProductGuarantee.objects.get(guarantee_code=1234567123)
        self.assertEqual(len(str(prod_guarantee_1.guarantee_code)), 10)
        self.assertEqual(len(str(prod_guarantee_2.guarantee_code)), 10)


class ProductServiceTestCase(TestCase):
    def setUp(self) -> None:
        ServiceDiscount.objects.create(name='annual discount', percent=10, description='')
        ServiceDiscount.objects.create(name='monthly discount', percent=5, description='')
        ProductService.objects.create(service_name='LCD Repairment', description="", guarantee_support=True,
                                      discount=ServiceDiscount.objects.get(id=1))
        ProductService.objects.create(service_name='A repair', description="No description", guarantee_support=True,
                                      discount=ServiceDiscount.objects.get(id=2))

    def test_product_service_qty(self):
        """This test counts number of services which support guarantee"""
        qty = len(ProductService.objects.filter(guarantee_support=True))
        self.assertEqual(qty, 2)

    def test_product_service_discount(self):
        prod_serv_1 = ProductService.objects.get(service_name='A repair')
        self.assertIsInstance(prod_serv_1.discount, ServiceDiscount)


class ServiceDiscountTestCase(TestCase):
    def setUp(self) -> None:
        ServiceDiscount.objects.create(name='annual discount', percent=10, description='')
        ServiceDiscount.objects.create(name='monthly discount', percent=5, description='')

    def service_discount_name(self):
        discount_1 = ServiceDiscount.objects.get(percent=10)
        discount_2 = ServiceDiscount.objects.get(percent=5)
        self.assertEqual(discount_1.name, 'annual discount')
        self.assertEqual(discount_2.name, 'monthly discount')
