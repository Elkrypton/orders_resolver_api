# Generated by Django 5.0.2 on 2024-03-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_resolver_api_core', '0002_delete_damage_remove_order_delivered_order_damage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('Preparing for shippment', '0001'), ('SHIPPED', '0002'), ('OUT FOR DELIVERY', '0003'), ('DELIVERED', '0004')], max_length=233),
        ),
    ]
