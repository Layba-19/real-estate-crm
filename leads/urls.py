from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('add/', views.add_lead, name='add_lead'),
    path('edit/<int:pk>/', views.edit_lead, name='edit_lead'),
    path('delete/<int:pk>/', views.delete_lead, name='delete_lead'),
]