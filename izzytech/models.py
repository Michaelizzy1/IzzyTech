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

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    CHOICES = [
        ('option1', 'Web Design'),
        ('option2', 'Graphics Design'),
        ('option3', 'Software Development'),
        ('option4', 'Mobile App Development'),
    ]
    NATURE = [
        ('option1', 'onsite'),
        ('option2', 'online'),
    ]
    desired_course = models.CharField(max_length=25, choices=CHOICES)
    mode_of_study = models.CharField(max_length=25, choices=NATURE)

    def __str__(self):
        return self.name