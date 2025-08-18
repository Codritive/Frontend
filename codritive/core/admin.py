from django.contrib import admin
from .models import About, Logo, Contact_Us, Get_InTouch, Our_Team
# Register your models here.

admin.site.register(Logo)
admin.site.register(About)
admin.site.register(Contact_Us)
admin.site.register(Our_Team)