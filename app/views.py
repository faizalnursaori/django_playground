from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, email=email, password=password)

        print(f"Succes Create New User: {new_user}")
        return redirect('login')
    
class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticate_user = authenticate(request, username=username, password=password)    
        if authenticate_user is None:
            messages.error(request, "Invalid Username or Password")
            return render(request, 'auth/login.html')

        login(request, authenticate_user)
        return redirect('dashboard_home')