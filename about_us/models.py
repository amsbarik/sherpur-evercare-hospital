from django.db import models

from core.models import BaseModel

# Create your models here.

class AboutUs(BaseModel):
    heading = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='about_us/')
    mission = models.TextField()
    vision = models.TextField()
    short_message = models.TextField()
    video_url = models.URLField(blank=True, default='https://')

    def __str__(self):
        return 'About Us'
