from django.shortcuts import render

from django.views.decorators.http import require_GET, require_POST

from service.models import Department, Service
from doctor.models import Doctor
from .models import Appointment

# Create your views here.

def appointment(request):
    departments = Department.objects.filter(is_active=True)

    return render(request, 'appointment/appointment.html', {'departments': departments})






from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from .models import DoctorSchedule


# def appointment_create_view(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)

#         if form.is_valid():
#             appointment = form.save(commit=False)

#             schedule_id = request.POST.get('schedule')
#             schedule = DoctorSchedule.objects.get(id=schedule_id)

#             appointment.appointment_time = schedule.start_time

#             try:
#                 appointment.full_clean()
#                 appointment.save()
#                 messages.success(request, 'Appointment booked successfully.')
#                 return redirect('appointment_create')
#             except ValidationError as e:
#                 form.add_error(None, e)
#     else:
#         form = AppointmentForm()

#     return render(request, 'appointment/appointment.html', {'form': form})
#     # return render(request, 'appointments/appointment_form.html', {'form': form})



# from django.contrib import messages
# from django.core.exceptions import ValidationError
# from django.shortcuts import render, redirect, get_object_or_404

# from .forms import AppointmentForm
# from .models import DoctorSchedule


# def appointment_create_view(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)

#         if form.is_valid():
#             appointment = form.save(commit=False)

#             schedule_id = form.cleaned_data.get('schedule')

#             schedule = get_object_or_404(
#                 DoctorSchedule,
#                 id=schedule_id
#             )

#             appointment.appointment_time = schedule.start_time

#             try:
#                 appointment.full_clean()
#                 appointment.save()

#                 messages.success(
#                     request,
#                     "Appointment booked successfully."
#                 )

#                 return redirect('appointment_create')

#             except ValidationError as e:
#                 form.add_error(None, e)

#     else:
#         form = AppointmentForm()

#     return render(
#         request,
#         'appointment/appointment.html',
#         {'form': form}
#     )







@require_POST
def book_appointment(request):
    try:
        appointment = Appointment(
            patient_name=request.POST.get("patient_name"),
            patient_phone=request.POST.get("patient_phone"),
            patient_email=request.POST.get("patient_email", ""),
            patient_address=request.POST.get("patient_address", ""),
            department_id=request.POST.get("department"),
            doctor_id=request.POST.get("doctor"),
            schedule_id=request.POST.get("schedule"),
            notes=request.POST.get("notes", ""),
        )

        appointment.full_clean()
        appointment.save()

        messages.success(request, "আপনার অ্যাপয়েন্টমেন্ট সফলভাবে বুক করা হয়েছে।")

    except Exception as e:
        messages.error(request, str(e))

    return redirect(request.META.get("HTTP_REFERER", "/"))




# @require_POST
# def book_appointment(request):
#     try:
#         department = Department.objects.get(id=request.POST.get("department"))
#         doctor = Doctor.objects.get(id=request.POST.get("doctor"))
#         schedule = DoctorSchedule.objects.get(id=request.POST.get("schedule"))

#         appointment = Appointment(
#             patient_name=request.POST.get("patient_name"),
#             patient_phone=request.POST.get("patient_phone"),
#             patient_email=request.POST.get("patient_email", ""),
#             patient_address=request.POST.get("patient_address", ""),
#             department=department,
#             doctor=doctor,
#             schedule=schedule,
#             # appointment_date=request.POST.get("appointment_date"),
#             # appointment_time=schedule.start_time,
#             notes=request.POST.get("notes", ""),
#         )

#         appointment.full_clean()
#         appointment.save()

#         messages.success(request, "Appointment booked successfully.")

#     except Exception as e:
#         messages.error(request, str(e))

#     return redirect(request.META.get("HTTP_REFERER", "/"))
















# from django.contrib import messages
# from django.core.exceptions import ValidationError
# from django.http import JsonResponse
# from django.shortcuts import redirect, render

# from .forms import AppointmentForm
# from .models import Appointment, Doctor, DoctorSchedule


# DAY_MAP = {
#     'Saturday': 'Saturday',
#     'Sunday': 'Sunday',
#     'Monday': 'Monday',
#     'Tuesday': 'Tuesday',
#     'Wednesday': 'Wednesday',
#     'Thursday': 'Thursday',
#     'Friday': 'Friday',
# }


# def appointment_create_view(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             try:
#                 appointment.full_clean()
#                 appointment.save()
#                 messages.success(request, 'Appointment booked successfully.')
#                 return redirect('appointment_create')
#             except ValidationError as e:
#                 form.add_error(None, e)
#     else:
#         form = AppointmentForm()

#     return render(request, 'appointment/appointment.html', {'form': form})
#     # return render(request, 'appointments/appointment_form.html', {'form': form})

