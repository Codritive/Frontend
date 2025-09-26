from django.shortcuts import render, get_object_or_404, redirect
from .models import Logo, About, Our_Team
from lessons.models import Course
from .forms import ContactForm
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

def tutor_detail(request, pk):
    team_member = get_object_or_404(Our_Team, pk=pk)

    return render(request, 'core/tutor.html', {
        'team_member': team_member
    })

# def our_team(request):
#     team_members = Our_Team.objects.all()
#     return render(request, 'core/team.html', {
#         'team': team_members
#     })

def logo(request):
    logo = Logo.objects.first()

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

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # reset the form after success
            print("Form is valid, message saved.")
        else:
            print("Form errors:", form.errors)
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'success': success
    })