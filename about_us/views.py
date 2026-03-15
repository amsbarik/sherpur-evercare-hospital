from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from core.views import is_superuser

from .forms import AboutUsForm
from . models import AboutUs

# Create your views here.





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