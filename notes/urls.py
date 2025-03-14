from django.urls import path
from .views import dashboard_home_view, dashboard_orders_view, dashboard_profile_view

urlpatterns = [
    path('', dashboard_home_view, name="dashboard_home"),
    path('orders/', dashboard_orders_view, name='dashboard_orders'),
    path('profile/', dashboard_profile_view, name='dashboard_profile')
]
