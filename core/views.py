from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Prefetch
from django.contrib import messages

from user_auth.views import is_superuser
from service.models import Service, Department
from about_us.models import AboutUs
from blog.models import Blog
from doctor.models import Doctor

from .models import HeroOverview, SiteSetting, Message, Subscribe
from .forms import HeroOverviewForm, SiteSettingForm, MessageForm





# Create your views here.

def index(request):

    hero_overview = HeroOverview.objects.first()
    message = Message.objects.first()
    about_us = AboutUs.objects.first()
    departments = Department.objects.filter(is_active=True).order_by('order', 'created_at')
    services = Service.objects.filter(is_active=True).order_by('order')[:11]
    blogs = Blog.objects.filter(is_active=True).order_by('order')[:3]

    department_doctors = Department.objects.filter(is_active=True).order_by('order')[:7].prefetch_related(
        Prefetch(
            'doctors',
            queryset=Doctor.objects.filter(is_active=True).order_by('order')[:1],
            to_attr='limited_doctors'  # important
        )
    )
    # doctors = Doctor.objects.filter(is_active=True).order_by('order')[:8]

    context = {
        'hero_overview': hero_overview,
        'message': message,
        'about_us': about_us,
        'departments': departments,
        'services': services,
        'blogs': blogs,
        'department_doctors': department_doctors,
    }

    return render(request, 'core/index.html', context)







def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('subscribe-email', '').strip()

        if email:
            obj, created = Subscribe.objects.get_or_create(email=email)

            if created:
                messages.success(request, "সফলভাবে সাবস্ক্রাইব করা হয়েছে!")
            else:
                messages.info(request, "আপনি ইতিমধ্যেই সাবস্ক্রাইব করেছেন।")

        else:
            messages.error(request, "অনুগ্রহ করে একটি বৈধ ইমেল প্রবেশ করান।")

    return redirect(request.META.get('HTTP_REFERER', '/'))




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



@login_required
@user_passes_test(is_superuser)
def message_form(request):
    message = Message.objects.first()

    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect("message_form")
    else:
        form = MessageForm(instance=message)


    return render(request, "core/admin/message_form.html", {"form": form})



@login_required
@user_passes_test(is_superuser)
def site_setting_form(request):
    setting = SiteSetting.objects.first()

    if request.method == "POST":
        form = SiteSettingForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()
            return redirect("site_setting_form")
    else:
        form = SiteSettingForm(instance=setting)


    return render(request, "core/admin/site_setting_form.html", {"form": form})


@login_required
@user_passes_test(is_superuser)
def subscribe_list(request):
    subscribers = Subscribe.objects.order_by('created_at').all()
    return render(request, 'core/admin/subscribe_list.html', {'subscribers': subscribers})
