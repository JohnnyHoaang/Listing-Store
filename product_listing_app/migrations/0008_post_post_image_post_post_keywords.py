# Generated by Django 4.0.3 on 2022-04-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing_app', '0007_alter_post_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='post_keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
