from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_order, name='new_order'),
    path('edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('print/<int:pk>/', views.print_order, name='print_order'),
]