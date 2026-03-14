from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


from core.views import is_superuser

from .models import Service, Department
from .forms import ServiceForm, DepartmentForm

# Create your views here.










# ///////////////////////////////////////
# admin panel views 

@login_required
@user_passes_test(is_superuser)
def department_list(request):
    departments = Department.objects.order_by('created_at').all()
    
    return render(request, 'service/admin/department_list.html', {'departments': departments})


# Departments create & update form view 
@login_required
@user_passes_test(is_superuser)
def department_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = DepartmentForm()
        else:
            department = Department.objects.get(id=pk)
            form = DepartmentForm(instance=department)
            
        return render(request, 'service/admin/department_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = DepartmentForm(request.POST, request.FILES)
        else:
            department = Department.objects.get(id=pk)
            form = DepartmentForm(request.POST, request.FILES, instance=department)

        if form.is_valid():
            form.save()
            
        return redirect('department_list')



# Service 
@login_required
@user_passes_test(is_superuser)
def service_list(request):
    services = Service.objects.order_by('created_at').all()
    
    return render(request, 'service/admin/service_list.html', {'services': services})


# Service create & update form view 
@login_required
@user_passes_test(is_superuser)
def service_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ServiceForm()
        else:
            service = Service.objects.get(id=pk)
            form = ServiceForm(instance=service)
            
        return render(request, 'service/admin/service_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ServiceForm(request.POST, request.FILES)
        else:
            service = Service.objects.get(id=pk)
            form = ServiceForm(request.POST, request.FILES, instance=service)

        if form.is_valid():
            form.save()
            
        return redirect('service_list')