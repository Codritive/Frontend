from django.db import models
from core.models import Our_Team

# Create your models here.
class Course(models.Model):
    COURSE_CHLOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Cybersecurity', 'Cybersecurity'),
        ('QA Testing', 'QA Testing'),
        ('SMM', 'SMM'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=COURSE_CHLOICES)
    short_description = models.TextField()
    full_description = models.TextField()
    lesson_duration_month= models.IntegerField()
    lesson_duration_minutes = models.IntegerField()
    tutor = models.ForeignKey(Our_Team, on_delete=models.SET_NULL, null=True)
    curriculum = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Courses"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question