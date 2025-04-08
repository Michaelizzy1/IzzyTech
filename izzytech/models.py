from django.db import models

# Create your models here.

class GraphicsModel(models.Model):
    image = models.ImageField(upload_to='grahics')


class WebModel(models.Model):
    image = models.ImageField(upload_to='web')


class SoftwareModel(models.Model):
    image = models.ImageField(upload_to='software')


class MobileModel(models.Model):
    image = models.ImageField(upload_to='mobile')


class MessageModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()