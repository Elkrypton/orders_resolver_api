# Generated by Django 5.0.2 on 2024-03-17 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_resolver_api_core', '0003_alter_order_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders_resolver_api_core.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders_resolver_api_core.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders_resolver_api_core.retail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders_resolver_api_core.vendor'),
        ),
    ]
