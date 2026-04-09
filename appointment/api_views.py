from django.http import JsonResponse

from doctor.models import Doctor, DoctorSchedule



from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from datetime import datetime

from .models import Department, Doctor, DoctorSchedule, Appointment


@require_GET
def ajax_load_doctors(request):
    department_id = request.GET.get("department_id")

    doctors = Doctor.objects.filter(
        department_id=department_id,
        is_available=True
    ).values("id", "name", "designation")

    return JsonResponse(list(doctors), safe=False)


# @require_GET
# def ajax_load_schedules(request):
#     doctor_id = request.GET.get("doctor_id")
#     appointment_date = request.GET.get("appointment_date")

#     if not doctor_id or not appointment_date:
#         return JsonResponse([], safe=False)

#     day_name = datetime.strptime(appointment_date, "%Y-%m-%d").strftime("%A")

#     schedules = DoctorSchedule.objects.filter(
#         doctor_id=doctor_id,
#         day_of_week=day_name
#     ).values(
#         "id",
#         "day_of_week",
#         "start_time",
#         "end_time"
#     )

#     return JsonResponse(list(schedules), safe=False)


@require_GET
def ajax_load_schedules(request):
    doctor_id = request.GET.get("doctor_id")

    schedules = DoctorSchedule.objects.filter(
        doctor_id=doctor_id, is_active=True
    ).values(
        "id",
        "day_of_week",
        "start_time",
        "end_time"
    )

    return JsonResponse(list(schedules), safe=False)
















# def doctors_by_department_api(request):
#     department_id = request.GET.get('department_id')

#     doctors = Doctor.objects.filter(
#         department_id=department_id,
#         is_available=True
#     ).values('id', 'name', 'designation')

#     return JsonResponse({'doctors': list(doctors)})



# def schedules_by_doctor_api(request):
#     doctor_id = request.GET.get('doctor_id')

#     schedules = DoctorSchedule.objects.filter(doctor_id=doctor_id).values(
#         'id',
#         'day_of_week',
#         'start_time',
#         'end_time'
#     )

#     return JsonResponse({'schedules': list(schedules)})





# # AJAX: Load doctors by department
# def doctors_by_department_api(request):
#     department_id = request.GET.get('department_id')
#     doctors = Doctor.objects.filter(
#         department_id=department_id,
#         is_available=True
#     ).values('id', 'name', 'designation')

#     return JsonResponse({'doctors': list(doctors)})



# # AJAX: Load schedules by doctor
# def schedules_by_doctor_api(request):
#     doctor_id = request.GET.get('doctor_id')

#     schedules = DoctorSchedule.objects.filter(doctor_id=doctor_id).values(
#         'id',
#         'day_of_week',
#         'start_time',
#         'end_time',
#         'max_patients'
#     )

#     return JsonResponse({'schedules': list(schedules)})
