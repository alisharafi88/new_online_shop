# Generated by Django 4.2.5 on 2023-10-19 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_average_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_discount',
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.shop'),
        ),
    ]
