# Generated by Django 3.0.8 on 2021-07-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepcell', '0018_auto_20210701_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlVeteran',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(help_text='Volunteer year which we want to display', max_length=50)),
            ],
        ),
    ]