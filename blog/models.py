from django.db import models
from core.models import BaseModel


# BlogCategory
class BlogCategory(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

# Blog
class Blog(BaseModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name="blogs")
 
    intro = models.TextField()
    cover_photo = models.ImageField(upload_to='blogs/')
    published_at = models.DateTimeField(null=True, blank=True)

    # for details page 
    gallery_title = models.CharField(max_length=150, blank=True)
    gallery_image_01 = models.ImageField(upload_to='blogs/', blank=True, null=True)
    gallery_image_02 = models.ImageField(upload_to='blogs/', blank=True, null=True)
    gallery_image_03 = models.ImageField(upload_to='blogs/', blank=True, null=True)

    highlight_title = models.CharField(max_length=150, blank=True)
    key_point_01 = models.CharField(max_length=100, blank=True)
    key_point_02 = models.CharField(max_length=100, blank=True)
    key_point_03 = models.CharField(max_length=100, blank=True)
    key_point_04 = models.CharField(max_length=100, blank=True)
    key_point_05 = models.CharField(max_length=100, blank=True)
    key_point_06 = models.CharField(max_length=100, blank=True)
    key_point_07 = models.CharField(max_length=100, blank=True)
    
    comment = models.TextField(blank=True)
    paragraph_01 = models.TextField(blank=True)
    paragraph_02 = models.TextField(blank=True)
    paragraph_03 = models.TextField(blank=True)
    paragraph_04 = models.TextField(blank=True)
    paragraph_05 = models.TextField(blank=True)

    @property
    def published_ago(self):
        # Human readable publish time (e.g. '4 months ago').
        if self.published_at:
            from django.utils.timesince import timesince
            return timesince(self.published_at) + " ago"
        return "Not published yet"
    

    def __str__(self):
        return self.title
