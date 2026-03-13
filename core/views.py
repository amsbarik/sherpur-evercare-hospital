from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from user_auth.views import is_superuser

from .models import HeroOverview
from .forms import HeroOverviewForm



# Create your views here.

def index(request):

    return render(request, 'core/index.html')




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



