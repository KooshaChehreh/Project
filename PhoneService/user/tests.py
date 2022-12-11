from django.test import TestCase
from .models import User, Profile, Address


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="koosha", password="Qwerty1234", is_staff=False)
        User.objects.create(username="reza", password="Qwerty9876", is_staff=True)

    def test_user_is_staff(self):
        """whether users are staff or not correctly identified"""
        user1 = User.objects.get(username="koosha")
        user2 = User.objects.get(username="reza")
        self.assertEqual(user1.is_staff, False)
        self.assertEqual(user2.is_staff, True)

    def test_user_creation(self):
        user1 = User.objects.get(username="koosha")
        if user1 is not None:
            test_value = True
            self.assertTrue(test_value, 'User was created!')

    def test_username_max_length(self):
        user1 = User.objects.get(username='koosha')
        max_length = user1._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)


class ProfileTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="koosha", password="Qwerty1234", is_staff=False)
        user2 = User.objects.create(username="reza", password="Qwerty9876", is_staff=True)
        Profile.objects.create(phone='09123456789', email='koosha@gmail.com', user=user1)
        Profile.objects.create(phone='09123451234', email='reza@gmail.com', user=user2)

    def test_profile_phone(self):
        profile1 = Profile.objects.get(email='koosha@gmail.com')
        profile2 = Profile.objects.get(email='reza@gmail.com')
        self.assertEqual(profile1.phone, '09123456789')
        self.assertEqual(profile2.phone, '09123451234')


class AddressTestCase(TestCase):
    def setUp(self):
        user2 = User.objects.create(username="reza", password="Qwerty9876", is_staff=True)
        Address.objects.create(latitude=123442, longitude=234235, city='Babol',
                               district='1', description='', user=user2)

    def test_address_raise_value_error(self):
        user1 = User.objects.create(username="koosha", password="Qwerty1234", is_staff=False)
        with self.assertRaises(ValueError):
            Address.objects.create(latitude="", longitude="234324", city='Tehran',
                                   district='3', description='', user=user1)

    def test_address_user_password(self):
        address1 = Address.objects.get(latitude=123442)
        self.assertEqual(address1.user.password, "Qwerty9876")
