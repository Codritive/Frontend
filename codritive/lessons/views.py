from django.shortcuts import render
from .models import Course, FAQ
# Create your views here.


def training(request):
    courses = Course.objects.all()
    return render(request, 'lessons/trainings.html', {
        'courses': courses
    })

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'lessons/faq.html', {
        'faqs': faqs
    })