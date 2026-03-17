from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from core.views import is_superuser

from .models import Hospital, Specialization, Doctor, DoctorSchedule
from .forms import HospitalForm, SpecializationForm, DoctorForm, DoctorScheduleForm

# Create your views here.












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
    doctors = Doctor.objects.select_related('department').prefetch_related('hospitals', 'specializations').order_by('created_at')
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











