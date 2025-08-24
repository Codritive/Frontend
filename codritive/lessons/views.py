from django.shortcuts import render, get_object_or_404
from .models import Course, FAQ
# Create your views here.


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'core/training.html', {
        'courses': courses
        })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'lessons/trainings.html', {
        'course': course
        })
    