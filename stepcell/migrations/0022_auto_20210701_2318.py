# Generated by Django 3.0.8 on 2021-07-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepcell', '0021_auto_20210701_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='fb_link',
            field=models.CharField(blank=True, default='#', help_text='facebook profile link', max_length=300),
        ),
        migrations.AlterField(
            model_name='team',
            name='insta_link',
            field=models.CharField(blank=True, default='#', help_text='instagram profile link', max_length=300),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_link',
            field=models.CharField(blank=True, default='#', help_text='linkedin profile link', max_length=300),
        ),
        migrations.AlterField(
            model_name='team',
            name='yt_link',
            field=models.CharField(blank=True, default='#', help_text='youtube channel link', max_length=300),
        ),
    ]
