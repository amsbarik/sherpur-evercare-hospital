from django.shortcuts import render

# Create your views here.

def blood_donors(request):
    return render(request, 'blood_bank/blood_donors.html')