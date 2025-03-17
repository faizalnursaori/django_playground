from django.shortcuts import redirect, render
from .models import Notes
from django.contrib import messages
from django.views import View

class NotesView(View):
    def get(self, request):
        notes = Notes.objects.all()
        context = {
            "notes": notes
        }

        return render(request, 'dashboard/dashboard_notes.html', context)

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Notes.objects.create(title=title, content=content)
            messages.success(request, "Succes add notes")
        else:
            messages.error(request, "Title and Content are required")

        return redirect('dashboard_notes')

# Create your views here.
def dashboard_home_view(request):
    return render(request, 'dashboard/dashboard_home.html')

def dashboard_orders_view(request):
    return render(request, 'dashboard/dashboard_orders.html')

# def dashboard_notes_view(request):
#     notes = Notes.objects.all()
#     context = {
#         "notes": notes
#     }

#     return render(request, 'dashboard/dashboard_notes.html', context)

def notes_detail_view(request, id):
    notes = Notes.objects.get(id=id)
    context = {
        "notes": notes
    }
    return render(request, 'dashboard/notes_details.html', context)

def dashboard_profile_view(request):
    return render(request, 'dashboard/dashboard_profile.html')
