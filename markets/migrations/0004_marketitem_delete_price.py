# Generated by Django 5.1.5 on 2025-01-25 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0003_alter_market_created_at_alter_price_created_at'),
        ('products', '0012_alter_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='market_items', to='markets.market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
