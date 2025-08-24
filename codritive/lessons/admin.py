from django.contrib import admin
from .models import Course
from core.models import Our_Team

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tutor')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tutor":
            if request.resolver_match.kwargs.get('object_id'):
                course_id = request.resolver_match.kwargs['object_id']
                from .models import Course
                try:
                    course = Course.objects.get(pk=course_id)
                    if course.category == "QA":
                        kwargs["queryset"] = Our_Team.objects.filter(position="QA Specialist")
                    elif course.category == "Python":
                        kwargs["queryset"] = Our_Team.objects.filter(position="Python Mentor")
                    elif course.category == "UI/UX":
                        kwargs["queryset"] = Our_Team.objects.filter(position="UI/UX Designer")
                except Course.DoesNotExist:
                    pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Course, CourseAdmin)
# Register your models here.