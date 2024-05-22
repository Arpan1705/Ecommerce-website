# Generated by Django 5.0.1 on 2024-03-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingsite', '0005_product_image_6'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]