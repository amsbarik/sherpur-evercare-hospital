from django.db import models
from django.utils import timezone
from datetime import date


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
    photo = models.ImageField(upload_to='blood_donors/', blank=True)

    last_donated = models.DateField(null=True, blank=True)
    # is_available = models.BooleanField(default=True)

    def last_donated_text(self):
        if not self.last_donated:
            return "সর্বশেষ ৩ মাসে রক্ত দান করেননি"
            # return "এখনো রক্ত দান করেননি"

        today = date.today()
        diff = (today - self.last_donated).days

        months = diff // 30

        if months == 0:
            return "এই মাসে রক্ত দান করেছেন"
        elif months == 1:
            return "সর্বশেষ ১ মাস আগে রক্ত দান করেছেন"
        else:
            return f"সর্বশেষ {months} মাস আগে রক্ত দান করেছেন"
    

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
    








