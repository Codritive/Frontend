from django.urls import path
from . import views
from .models import Course

app_name = 'lessons'

urlpatterns = [
    path('trainings/', views.training, name='trainings'),
]