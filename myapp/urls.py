from django.urls import path, re_path
from . import views

urlpatterns = [
    path('read_file_text/', views.read_file_text), #api URL
]