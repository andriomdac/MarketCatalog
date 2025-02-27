# Generated by Django 5.1.5 on 2025-01-21 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=False)),
                ('markets', models.ManyToManyField(related_name='products', to='markets.market')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateField(auto_now_add=True, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='markets', to='markets.market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prices', to='products.product')),
            ],
        ),
    ]
