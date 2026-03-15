from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from user_auth.views import is_superuser

from service.models import Service, Department
from about_us.models import AboutUs
from blog.models import Blog

from .models import HeroOverview
from .forms import HeroOverviewForm



# Create your views here.

def index(request):

    hero_overview = HeroOverview.objects.first()
    about_us = AboutUs.objects.first()
    departments = Department.objects.filter(is_active=True).order_by('order')[:12]
    services = Service.objects.filter(is_active=True).order_by('order')[:11]
    blogs = Blog.objects.filter(is_active=True).order_by('order')[:3]

    context = {
        'hero_overview': hero_overview,
        'about_us': about_us,
        'departments': departments,
        'services': services,
        'blogs': blogs,
    }

    return render(request, 'core/index.html', context)




# //////////////////////////////////////
# admin panel views start 


@login_required
@user_passes_test(is_superuser)
def hero_overview_form(request):
    hero = HeroOverview.objects.first()

    if request.method == "POST":
        form = HeroOverviewForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            return redirect("hero_overview_form")
    else:
        form = HeroOverviewForm(instance=hero)


    return render(request, "core/admin/hero_overview_form.html", {"form": form})



