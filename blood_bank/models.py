from django.db import models


from core.models import BaseModel

# Create your models here.



class BloodDonor(BaseModel):

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='blood_donors/', blank=True, default='img/user-icon.png')

    last_donated = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.name} ({self.blood_group})"