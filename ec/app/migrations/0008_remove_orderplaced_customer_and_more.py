# Generated by Django 4.1.7 on 2023-05-10 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='ordered_date',
        ),
    ]
