from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

from core.views import is_superuser
from service.models import Department

from .models import Hospital, Specialization, Doctor, DoctorSchedule
from .forms import HospitalForm, SpecializationForm, DoctorForm, DoctorScheduleForm



# Create your views here.


def doctors(request, slug=None):
    doctors = Doctor.objects.filter(is_active=True)

    department = None
    query = request.GET.get('search_query', '').strip()
    specializations = request.GET.getlist('specialization')  # 🔥 multiple
    genders = request.GET.getlist('gender')  # 🔥 multiple

    # 🔹 Department filter
    if slug:
        department = get_object_or_404(Department, slug=slug)
        doctors = doctors.filter(department=department)

    # 🔹 Search
    if query:
        doctors = doctors.filter(
            Q(name__icontains=query) |
            Q(designation__icontains=query) |
            Q(specializations__name__icontains=query)
        )

    # 🔹 Specialization filter
    if specializations:
        doctors = doctors.filter(specializations__id__in=specializations)

    # 🔹 Gender filter
    if genders:
        doctors = doctors.filter(gender__in=genders)

    doctors = doctors.distinct().order_by('order')

    context = {
        'doctors': doctors,
        'department': department,
        'query': query,
        'selected_specializations': specializations,
        'selected_genders': genders,
        'all_specializations': Specialization.objects.all(),
    }

    return render(request, 'doctor/doctors.html', context)







# def doctors(request, slug=None):
#     doctors = Doctor.objects.filter(is_active=True)

#     department = None
#     query = request.GET.get('search_query')

#     # 🔹 Department filter
#     if slug:
#         department = get_object_or_404(Department, slug=slug)
#         doctors = doctors.filter(department=department)

#     # 🔹 Search filter
#     if query:
#         doctors = doctors.filter(
#             Q(name__icontains=query) |
#             Q(designation__icontains=query) |
#             Q(specializations__name__icontains=query)
#         ).distinct()

#     doctors = doctors.order_by('order')

#     context = {
#         'doctors': doctors,
#         'department': department,
#         'query': query,
#     }

#     return render(request, 'doctor/doctors.html', context)




# def doctors(request):

#     doctors = Doctor.objects.filter(is_active=True).order_by('order')

#     context = {
#         'doctors': doctors,
#     }

#     return render(request, 'doctor/doctors.html', context)





# doctor_details
def doctor_details(request, slug):

    return render(request, 'doctor/doctor_details.html')









# admin views ////////////////////////

# Hospital 
@login_required
@user_passes_test(is_superuser)
def hospital_list(request):
    hospitals = Hospital.objects.order_by('created_at').all()
    return render(request, 'doctor/admin/hospital_list.html', {'hospitals': hospitals})


@login_required
@user_passes_test(is_superuser)
def hospital_form(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            form = HospitalForm()
        else:
            hospital = Hospital.objects.get(id=pk)
            form = HospitalForm(instance=hospital)

        return render(request, 'doctor/admin/hospital_form.html', {'form': form})

    else:
        if pk == 0:
            form = HospitalForm(request.POST, request.FILES)
        else:
            hospital = Hospital.objects.get(id=pk)
            form = HospitalForm(request.POST, request.FILES, instance=hospital)

        if form.is_valid():
            form.save()

        return redirect('hospital_list')
    


# Specialization 
@login_required
@user_passes_test(is_superuser)
def specialization_list(request):
    specializations = Specialization.objects.order_by('created_at').all()
    return render(request, 'doctor/admin/specialization_list.html', {'specializations': specializations})


@login_required
@user_passes_test(is_superuser)
def specialization_form(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            form = SpecializationForm()
        else:
            specialization = Specialization.objects.get(id=pk)
            form = SpecializationForm(instance=specialization)

        return render(request, 'doctor/admin/specialization_form.html', {'form': form})

    else:
        if pk == 0:
            form = SpecializationForm(request.POST)
        else:
            specialization = Specialization.objects.get(id=pk)
            form = SpecializationForm(request.POST, instance=specialization)

        if form.is_valid():
            form.save()

        return redirect('specialization_list')
    




# Doctor 
@login_required
@user_passes_test(is_superuser)
def doctor_list(request):
    doctors = Doctor.objects.select_related('department').prefetch_related('specializations').order_by('created_at')
    return render(request, 'doctor/admin/doctor_list.html', {'doctors': doctors})


@login_required
@user_passes_test(is_superuser)
def doctor_form(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            form = DoctorForm()
        else:
            doctor = Doctor.objects.get(id=pk)
            form = DoctorForm(instance=doctor)

        return render(request, 'doctor/admin/doctor_form.html', {'form': form})

    else:
        if pk == 0:
            form = DoctorForm(request.POST, request.FILES)
        else:
            doctor = Doctor.objects.get(id=pk)
            form = DoctorForm(request.POST, request.FILES, instance=doctor)

        # if form.is_valid():
        #     form.save()

        # return redirect('doctor_list')
    
        if form.is_valid():
            form.save()
            return redirect('doctor_list')   # ✅ must redirect
        else:
            print(form.errors)  # 🔥 DEBUG

    return redirect('doctor_list')
    




# Doctor Schedule
@login_required
@user_passes_test(is_superuser)
def doctor_schedule_list(request):
    schedules = DoctorSchedule.objects.select_related('doctor').order_by('created_at')
    return render(request, 'doctor/admin/doctor_schedule_list.html', {'schedules': schedules})


@login_required
@user_passes_test(is_superuser)
def doctor_schedule_form(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            form = DoctorScheduleForm()
        else:
            schedule = DoctorSchedule.objects.get(id=pk)
            form = DoctorScheduleForm(instance=schedule)

        return render(request, 'doctor/admin/doctor_schedule_form.html', {'form': form})

    else:
        if pk == 0:
            form = DoctorScheduleForm(request.POST)
        else:
            schedule = DoctorSchedule.objects.get(id=pk)
            form = DoctorScheduleForm(request.POST, instance=schedule)

        if form.is_valid():
            form.save()

        return redirect('doctor_schedule_list')











