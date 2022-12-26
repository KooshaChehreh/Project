# Generated by Django 4.1.4 on 2022-12-26 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_imei1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imei1',
            field=models.BigIntegerField(choices=[('Iphone', 'Iphone'), ('Samsung', 'Samsung'), ('Xiaomi', 'Xiaomi')], primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxLengthValidator(13), django.core.validators.MinLengthValidator(1)]),
        ),
    ]