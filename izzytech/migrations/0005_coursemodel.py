# Generated by Django 5.2 on 2025-04-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izzytech', '0004_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
