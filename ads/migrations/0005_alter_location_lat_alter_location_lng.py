# Generated by Django 4.1 on 2022-08-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_location_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
    ]
