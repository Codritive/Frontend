from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('training/', views.training, name='training'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
    path('get-in-touch/', views.get_in_touch, name='get_in_touch'),
    path('service/', views.service, name='service'),
    path("tutor/<int:pk>/", views.tutor_detail, name="tutor"),

]