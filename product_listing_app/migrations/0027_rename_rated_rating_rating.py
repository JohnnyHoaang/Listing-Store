# Generated by Django 4.0.4 on 2022-05-15 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing_app', '0026_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rated',
            new_name='rating',
        ),
    ]
