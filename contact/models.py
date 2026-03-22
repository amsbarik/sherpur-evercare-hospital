from django.db import models

from service.models import Service

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=250, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.mobile
    

