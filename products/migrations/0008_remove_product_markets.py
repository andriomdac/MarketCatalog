# Generated by Django 5.1.5 on 2025-01-24 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='markets',
        ),
    ]
