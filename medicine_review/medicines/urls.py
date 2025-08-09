from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('medicine/add/', views.medicine_add, name='medicine_add'),
    path('medicine/<int:pk>/edit/', views.medicine_edit, name='medicine_edit'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
]