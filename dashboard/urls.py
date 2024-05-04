from django.urls import path
from . import views #from current folder, import views

urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff')
]
