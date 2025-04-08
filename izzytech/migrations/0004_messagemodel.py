# Generated by Django 5.1.7 on 2025-04-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izzytech', '0003_mobilemodel_softwaremodel_webmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
