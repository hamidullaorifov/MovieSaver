from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    # year = models.PositiveIntegerField()
    date = models.DateField()
    description = models.TextField()
    video = models.FileField(upload_to='videos')
    picture = models.ImageField(upload_to='images')
