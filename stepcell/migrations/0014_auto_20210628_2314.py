# Generated by Django 3.0.8 on 2021-06-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepcell', '0013_auto_20210628_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abhivyaktievent',
            name='event_link',
            field=models.CharField(default='#', help_text='registration page link for the event', max_length=300, null=True),
        ),
    ]
