from django.shortcuts import render

# Create your views here.
def dashboard_home_view(request):
    return render(request, 'dashboard/dashboard_home.html')

def dashboard_orders_view(request):
    return render(request, 'dashboard/dashboard_orders.html')

def dashboard_profile_view(request):
    return render(request, 'dashboard/dashboard_profile.html')
