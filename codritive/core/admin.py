from django.contrib import admin
from .models import About, Logo, Contact_Us, Get_InTouch, Our_Team
from lessons.models import FAQ, Course
# Register your models here.

class Course_inline(admin.StackedInline):
    model = Course
    extra = 1
class Our_TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    inlines = [Course_inline]
    

admin.site.register(Logo)
admin.site.register(About)
admin.site.register(Contact_Us)
admin.site.register(Our_Team, Our_TeamAdmin)
