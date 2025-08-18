from django.shortcuts import render
from .models import Logo, About, Contact_Us, Our_Team, Get_InTouch
from lessons.models import Course
# Create your views here.
def index(request):
    return render(request, 'core/base.html')

def home(request):
    return render(request, 'core/home.html')

def service(request):
    return render(request, 'core/service.html')

def about(request):
    about_info = About.objects.first()
    team_members = Our_Team.objects.all()
    return render(request, 'core/about.html', {
        'about': about_info,
        'team_members': team_members
        })

def contact_us(request):
    contact_info = Contact_Us.objects.first()
    return render(request, 'core/contact.html', {
        'contact_us': contact_info
    })

def get_in_touch(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Get_InTouch.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )

    return render(request, 'core/contact.html',{
        'get_in_touch': Get_InTouch.objects.all()
    })

# def our_team(request):
#     team_members = Our_Team.objects.all()
#     return render(request, 'core/team.html', {
#         'team': team_members
#     })

def logo(request):
    logo = Logo.Objects.first()
    return render(request, 'core/base.html', {
        'logo': logo
    })

def trainings(request):
    courses = Course.objects.all()
    return render(request, 'lessons/trainings.html', {
        'courses': courses
    })

def training(request):
    courses = Course.objects.all()
    return render(request, 'core/training.html', {
        'courses': courses
        })