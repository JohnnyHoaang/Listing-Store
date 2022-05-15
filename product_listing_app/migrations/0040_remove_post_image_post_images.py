# Generated by Django 4.0.4 on 2022-05-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing_app', '0039_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
