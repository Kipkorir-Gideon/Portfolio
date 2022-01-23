from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Languages(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Projects(models.Model):
    title = models.CharField(max_length=100)
    screenshot = CloudinaryField('image')
    description = models.TextField()
    languages = models.ManyToManyField(Languages)
    site_url = models.URLField()

    def __str__(self):
        return self.title