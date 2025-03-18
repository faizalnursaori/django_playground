from django.urls import path
from .views import HomeView, OrdersView, ProfileView,NotesView, DetailView, DeleteView, UpdateView

urlpatterns = [
    path('', HomeView.as_view(), name="dashboard_home"),
    path('orders/', OrdersView.as_view(), name='dashboard_orders'),
    path('notes/', NotesView.as_view(), name='dashboard_notes'),
    path('profile/', ProfileView.as_view(), name='dashboard_profile'),
    path('notes/<str:id>', DetailView.as_view(), name='notes_detail_view'),
    path('notes/<str:id>/delete/', DeleteView.as_view(), name='delete'),
    path('notes/<str:id>/update/', UpdateView.as_view(), name='update')
]
