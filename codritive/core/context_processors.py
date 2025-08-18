from .models import Logo

def logo(request):
    return {'logo': Logo.objects.first()}