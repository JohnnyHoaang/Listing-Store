# Generated by Django 4.0.4 on 2022-04-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management_app', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
