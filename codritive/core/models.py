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

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=12,
        validators=[RegexValidator(
            r'^\+374\d{8}$',
            'Enter a valid Armenian phone number starting with +374 and followed by 8 digits.'
        )]
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.subject}'

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
    
