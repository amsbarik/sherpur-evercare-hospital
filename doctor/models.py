from django.db import models
from django.utils.text import slugify
from uuid import uuid4

from core.models import BaseModel
from service.models import Department


class Hospital(BaseModel):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    


class Specialization(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Doctor(BaseModel):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    slug = models.SlugField(unique=True, blank=True, help_text="Enter a unique English URL name using lowercase letters and hyphens (-) only. Example: dr-abdul-karim")

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctors")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors", blank=True, null=True)
    specializations = models.ManyToManyField(Specialization, related_name="doctors", blank=True, null=True) 

    designation = models.CharField(max_length=150)
    qualification = models.CharField(max_length=200)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    doctor_image = models.ImageField(upload_to="doctors/")
    bio = models.TextField(blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    is_available = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.name)

            # Bengali / non-English fallback
            if not base_slug:
                base_slug = f"doctor-{uuid4().hex[:8]}"

            slug = base_slug
            counter = 1

            while Doctor.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)



    def __str__(self):
        return self.name
    



class DoctorSchedule(BaseModel):
    # DAYS = [
    #     ("Saturday", "Saturday"),
    #     ("Sunday", "Sunday"),
    #     ("Monday", "Monday"),
    #     ("Tuesday", "Tuesday"),
    #     ("Wednesday", "Wednesday"),
    #     ("Thursday", "Thursday"),
    #     ("Friday", "Friday"),
    # ]
    DAYS = [
        ("Saturday", "শনিবার"),
        ("Sunday", "রবিবার"),
        ("Monday", "সোমবার"),
        ("Tuesday", "মঙ্গলবার"),
        ("Wednesday", "বুধবার"),
        ("Thursday", "বৃহস্পতিবার"),
        ("Friday", "শুক্রবার"),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="schedules")
    day_of_week = models.CharField(max_length=10, choices=DAYS, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_patients = models.PositiveIntegerField(default=20)

    is_7days = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day_of_week} ({self.start_time}-{self.end_time})"
    
































