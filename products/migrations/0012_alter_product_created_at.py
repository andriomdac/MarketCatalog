# Generated by Django 5.1.5 on 2025-01-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
