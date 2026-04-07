from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


from core.views import is_superuser
from .models import BloodDonor
from .forms import BloodDonorForm


# Create your views here.

from django.shortcuts import render, redirect
from .models import BloodDonor
from .forms import BloodDonorForm


def blood_donors(request):
    donors = BloodDonor.objects.all().order_by('-id')
    return render(request, 'blood_bank/blood_donors.html', {'donors': donors})


def blood_donor_form(request):
    if request.method == 'POST':
        form = BloodDonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blood_donors')
    else:
        form = BloodDonorForm()

    return render(request, 'blood_bank/blood_donor_form.html', {'form': form})








# admin views 


# BloodDonor list  
@login_required
@user_passes_test(is_superuser)
def blood_donor_list(request):
    blood_donors = BloodDonor.objects.order_by('created_at').all()
    
    return render(request, 'blood_bank/admin/blood_donor_list.html', {'blood_donors': blood_donors})



# blood_donor create & update form view 
@login_required
@user_passes_test(is_superuser)
def blood_donor_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = BloodDonorForm()
        else:
            donor = BloodDonor.objects.get(id=pk)
            form = BloodDonorForm(instance=donor)
            
        return render(request, 'blood_bank/admin/blood_donor_create_or_update.html', {'form': form})
    
    else:
        if pk == 0:
            form = BloodDonorForm(request.POST, request.FILES)
        else:
            donor = BloodDonor.objects.get(id=pk)
            form = BloodDonorForm(request.POST, request.FILES, instance=donor)

        if form.is_valid():
            form.save()
            
        return redirect('blood_donor_list')