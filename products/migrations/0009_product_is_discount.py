# Generated by Django 4.2.5 on 2023-09-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_is_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
    ]