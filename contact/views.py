from django.shortcuts import render, redirect
from django.contrib import messages

from service.models import Service

from .models import ContactUs



# Create your views here.

def contact_us(request):

    services = Service.objects.filter(is_active=True).order_by('order')

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        service_id = request.POST.get('service')
        message = request.POST.get('message')

        service_instance = None

        # 🔥 convert ID → instance safely
        if service_id and service_id.isdigit():
            service_instance = Service.objects.filter(id=service_id).first()

        ContactUs.objects.create(
            name=name,
            mobile=mobile,
            address=address,
            service=service_instance, 
            message=message
        )
        messages.success(request, 'আপনার বার্তা সফলভাবে পাঠানো হয়েছে!')
        return redirect('contact_us') 

    return render(request, 'contact/contact_us.html', {
        'services': services
    })





# admin views ////////////////////////////

def contact_list(request):

    messages = ContactUs.objects.order_by('created_at').all()

    return render(request, 'contact/admin/contact_list.html', {'messages': messages})