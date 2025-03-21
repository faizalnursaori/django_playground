from django.shortcuts import redirect, render
from .models import Notes
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        notes = Notes.objects.filter(actor=request.user)
        context = {
            "notes": notes
        }

        return render(request, 'dashboard/dashboard_notes.html', context)

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not title or not content:
            messages.error(request, "Title and Content are Required")
            context={
                "notes": Notes.objects.all(),
                "form_data":{
                    "title": title,
                    "content": content
                }
            }
            return render(request, "dashboard/dashboard_notes.html", context)
    
        Notes.objects.create(title=title, content=content, actor=request.user)
        messages.success(request, "Notes Added")
        return redirect('dashboard_notes')
    
class DetailView(View):
    def get(self, request, id):
        notes = Notes.objects.get(id=id)
        context = {
            "notes": notes
        }
        return render(request, 'dashboard/notes_details.html', context)

class DeleteView(View):
    def post(self, request, id):
        notes = Notes.objects.get(id=id)
        notes.delete()
        messages.success(request, "Succes delete notes")
        
        return redirect('dashboard_notes')

class UpdateView(View):
    def get(self, request, id):
        try:
            notes = Notes.objects.get(id=id)
            context = {
                "notes": notes
            }
            return render(request, 'dashboard/notes_edit.html', context)
        except Notes.DoesNotExist:
            messages.error(request, "Notes not found")
            return redirect('dashboard_notes')
    
    def post(self, request, id):
        try:
            notes = Notes.objects.get(id=id)
            
            # Ambil nilai dari form
            title = request.POST.get('title')
            content = request.POST.get('content')
            
            # Periksa validasi
            if not title or not content:
                messages.error(request, "Title and Content are required")
                # Gunakan objek yang TIDAK disimpan ke database dengan nilai dari form
                context = {
                    "notes": {
                        "id": id,
                        "title": title or "",  # Gunakan nilai input atau string kosong
                        "content": content or "",  # Gunakan nilai input atau string kosong
                    }
                }
                return render(request, 'dashboard/notes_edit.html', context)
            
            # Jika valid, simpan ke database
            notes.title = title
            notes.content = content
            notes.save()
            messages.success(request, "Success update notes")
            return redirect('dashboard_notes')
            
        except Notes.DoesNotExist:
            messages.error(request, "Notes not found")
            return redirect('dashboard_notes')
        

class HomeView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard_home.html')


class OrdersView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard_orders.html')
    
class ProfileView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard_profile.html')    
# Create your views here.
# def dashboard_home_view(request):
#     return render(request, 'dashboard/dashboard_home.html')

# def dashboard_orders_view(request):
#     return render(request, 'dashboard/dashboard_orders.html')

# def dashboard_notes_view(request):
#     notes = Notes.objects.all()
#     context = {
#         "notes": notes
#     }

#     return render(request, 'dashboard/dashboard_notes.html', context)

# def notes_detail_view(request, id):
#     notes = Notes.objects.get(id=id)
#     context = {
#         "notes": notes
#     }
#     return render(request, 'dashboard/notes_details.html', context)

# def dashboard_profile_view(request):
#     return render(request, 'dashboard/dashboard_profile.html')
