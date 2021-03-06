# Generated by Django 3.0.8 on 2021-07-01 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepcell', '0015_abhivyaktiperformingevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlVolunteer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(help_text='Veteran year which we want to display', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(default='', help_text='batch year, starting year to end year. It must be 4 years. e.g. 2018-2022', max_length=50)),
                ('student_name', models.CharField(help_text='student name', max_length=100)),
                ('branch', models.CharField(help_text='branch', max_length=200)),
                ('phone', models.IntegerField(blank=True, help_text='10 digits phone number')),
                ('fb_link', models.CharField(help_text='facebook profile link', max_length=300)),
                ('insta_link', models.CharField(help_text='instagram profile link', max_length=300)),
                ('yt_link', models.CharField(default='', help_text='youtube channel link', max_length=300)),
                ('image', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
            ],
        ),
    ]
