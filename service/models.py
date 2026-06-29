from django.db import models
from django.utils.text import slugify
from uuid import uuid4

from core.models import BaseModel

# Create your models here.

class Department(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, help_text="Enter a unique English URL name using lowercase letters and hyphens (-) only. Example: cardiology, neurology")
    department_icon = models.ImageField(upload_to='icons/', default='/icon.jpg')
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.name)

            # Bengali / non-English fallback
            if not base_slug:
                base_slug = f"department-{uuid4().hex[:8]}"

            slug = base_slug
            counter = 1

            while Department.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    


class Service(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, help_text="Enter a unique English URL name using lowercase letters and hyphens (-) only. Example: cardiology, neurology")
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="services")
    service_icon = models.ImageField(upload_to='icons/')
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name