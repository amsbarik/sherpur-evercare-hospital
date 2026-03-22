from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Prefetch

from core.views import is_superuser
from service.models import Department
from doctor.models import Doctor

from .forms import AboutUsForm
from . models import AboutUs

# Create your views here.


def about_us(request):

    about_us = AboutUs.objects.first()
    departments = Department.objects.filter(is_active=True).order_by('order')[:12]
    department_doctors = Department.objects.filter(is_active=True).order_by('order')[:7].prefetch_related(
        Prefetch(
            'doctors',
            queryset=Doctor.objects.filter(is_active=True).order_by('order')[:1],
            to_attr='limited_doctors'  # important
        )
    )

    context = {
        'about_us': about_us,
        'departments': departments,
        'department_doctors': department_doctors,
    }

    return render(request, 'about_us/about_us.html', context)



# admin views ///////////////////////////////////////////////
@login_required
@user_passes_test(is_superuser)
def about_create_or_update(request):
    about_us = AboutUs.objects.first()

    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect("about_create_or_update")
    else:
        form = AboutUsForm(instance=about_us)


    return render(request, "about_us/admin/about_us_form.html", {"form": form})