# Generated by Django 5.0.1 on 2024-02-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingsite', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
