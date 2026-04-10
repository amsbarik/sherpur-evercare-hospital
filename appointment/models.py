from django.db import models
from django.core.exceptions import ValidationError

from service.models import Department
from doctor.models import Doctor, DoctorSchedule
from core.models import BaseModel

# Create your models here.




from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class Appointment(BaseModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    patient_name = models.CharField(max_length=150)
    patient_phone = models.CharField(max_length=20)
    patient_email = models.EmailField(blank=True)
    patient_address = models.CharField(max_length=255, blank=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE, null=True, blank=True)

    # appointment_date = models.DateField(blank=True, null=True)
    # appointment_time = models.TimeField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    notes = models.TextField(blank=True)


    def clean(self):
        if self.doctor.department_id != self.department_id:
            raise ValidationError(
                "Selected doctor does not belong to this department."
            )

        if self.schedule.doctor_id != self.doctor_id:
            raise ValidationError(
                "Selected schedule does not belong to selected doctor."
            )
        

    # def clean(self):
    #     if not self.appointment_date:
    #         raise ValidationError("Appointment date is required.")

    #     day = self.appointment_date.strftime("%A")

    #     if self.doctor.department_id != self.department_id:
    #         raise ValidationError("Selected doctor does not belong to this department.")

    #     if self.schedule.doctor_id != self.doctor_id:
    #         raise ValidationError("Invalid schedule selected for doctor.")

    #     if self.schedule.day_of_week != day:
    #         raise ValidationError("Selected date does not match doctor's schedule.")
        


    # class Meta:
    #     unique_together = ("doctor", "appointment_date", "appointment_time")

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"
    







# class Appointment(BaseModel):
#     STATUS_CHOICES = [
#         ("pending", "Pending"),
#         ("confirmed", "Confirmed"),
#         ("completed", "Completed"),
#         ("cancelled", "Cancelled"),
#     ]

#     patient_name = models.CharField(max_length=150)
#     patient_phone = models.CharField(max_length=20)
#     patient_email = models.EmailField(blank=True)

#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    
#     appointment_date = models.DateField()
#     appointment_time = models.TimeField()

#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
#     notes = models.TextField(blank=True)

#     # check schedule validity 
#     # def clean(self):
#     #     day = self.appointment_date.strftime("%a").lower()

#     #     is_available = DoctorSchedule.objects.filter(
#     #         doctor=self.doctor,
#     #         day_of_week=day,
#     #         start_time__lte=self.appointment_time,
#     #         end_time__gte=self.appointment_time
#     #     ).exists()

#     #     if not is_available:
#     #         raise ValidationError("Doctor is not available at this time.")


#     def clean(self):
#         day = self.appointment_date.strftime('%A')

#         if self.doctor.department_id != self.department_id:
#             raise ValidationError('Selected doctor does not belong to this department.')

#         is_available = DoctorSchedule.objects.filter(
#             doctor=self.doctor,
#             day_of_week=day,
#             start_time__lte=self.appointment_time,
#             end_time__gte=self.appointment_time,
#         ).exists()

#         if not is_available:
#             raise ValidationError('Doctor is not available on selected date.')
        
        

#     # Prevent Double Booking
#     class Meta:  
#         unique_together = ("doctor", "appointment_date", "appointment_time")

#     def __str__(self):
#         return f"{self.patient_name} - {self.doctor.name} ({self.appointment_date})"
    






# Department.objects.get(slug="cardiology").doctors.all() 