# Generated by Django 4.1.4 on 2022-12-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product/%Y/%m/%d'),
        ),
    ]
