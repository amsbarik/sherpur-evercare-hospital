from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout

from django.views import View
from django.contrib import messages

from user_auth.views import is_superuser


# Create your views here.

@login_required(login_url='admin_login')
@user_passes_test(is_superuser)
def dashboard(request):

    return render(request, 'admin/dashboard.html')



class AdminLoginView(View):

    template_name = "admin/admin_login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)

            return redirect("dashboard")

        messages.error(request, "Invalid email or password")
        return redirect("admin_login")
    



# logout 
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_logout(request):
    logout(request)
    return redirect('index') 






















