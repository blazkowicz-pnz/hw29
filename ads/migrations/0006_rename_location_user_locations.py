# Generated by Django 4.1 on 2022-08-29 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='locations',
        ),
    ]
