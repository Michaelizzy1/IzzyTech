# Generated by Django 5.1.7 on 2025-04-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izzytech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicsmodel',
            name='image',
            field=models.ImageField(upload_to='grahics'),
        ),
    ]
