# Generated by Django 4.0.4 on 2022-05-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing_app', '0034_azureimage_myimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='azureimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
