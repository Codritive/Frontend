from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Logo(models.Model):
    image = models.ImageField(upload_to='logo_images/', blank=True, null=True)

    def __str__(self):
        return "Logo Image"
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    
class Contact_Us(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    contact_title = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    email = models.EmailField()
    address = models.TextField()
    working_hours = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.contact_title

class Get_InTouch(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
    
class Our_Team(models.Model):
    POSITION_CHOICES = [
        ('QA Specialist', 'QA Specialist'),
        ('Python Mentor', 'Python Mentor'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('JavaScript Mentor', 'JavaScript Mentor'),
        ('SMM Specialist', 'SMM Specialist'),
        ('Cybersecurity Mentor', 'Cybersecurity Mentor'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} - {self.position}"
    
