from django.shortcuts import render
from .models import Notes

# Create your views here.
def dashboard_home_view(request):
    return render(request, 'dashboard/dashboard_home.html')

def dashboard_orders_view(request):
    return render(request, 'dashboard/dashboard_orders.html')

def dashboard_notes_view(request):
    notes = Notes.objects.all()
    context = {
        "notes": notes
    }

    return render(request, 'dashboard/dashboard_notes.html', context)

def notes_detail_view(request, id):
    notes = Notes.objects.get(id=id)
    context = {
        "notes": notes
    }
    return render(request, 'dashboard/notes_details.html', context)

def dashboard_profile_view(request):
    return render(request, 'dashboard/dashboard_profile.html')
