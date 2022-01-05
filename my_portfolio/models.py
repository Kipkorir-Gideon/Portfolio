from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    screenshot = CloudinaryField('image')
    description = models.TextField()
    languages = models.CharField(max_length=255)
    site_url = models.URLField()