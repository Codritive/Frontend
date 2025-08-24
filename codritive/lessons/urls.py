from django.urls import path
from . import views
from .models import Course

app_name = 'lessons'

urlpatterns = [
    path('trainings/', views.courses_list, name='trainings'),
    path('trainings/<int:pk>/', views.course_detail, name='course_detail'),
]