from django.db import models
from django.utils.text import slugify
from core.models import BaseModel
from service.models import Department


class Hospital(BaseModel):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.address}'
    


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
    slug = models.SlugField(unique=True, blank=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctors")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors", blank=True, default=1)
    specializations = models.ManyToManyField(Specialization, related_name="doctors", blank=True) 

    designation = models.CharField(max_length=150)
    qualification = models.CharField(max_length=200)
    experience_years = models.PositiveIntegerField(blank=True)
    doctor_image = models.ImageField(upload_to="doctors/")
    bio = models.TextField(blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    is_available = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
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
    DAYS = [
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="schedules")
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_patients = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week}"
    
































