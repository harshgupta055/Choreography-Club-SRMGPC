# Generated by Django 3.0.8 on 2021-07-01 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepcell', '0023_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(help_text='Image dimension must be in 3:2 ratio', upload_to='gallery/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]