# Generated by Django 4.0.3 on 2022-04-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing_app', '0006_post_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
