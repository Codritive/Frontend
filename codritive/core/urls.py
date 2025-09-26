from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('training/', views.training, name='training'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path("tutor/<int:pk>/", views.tutor_detail, name="tutor"),
    path('contact/', views.contact_view, name='contact'),

]
