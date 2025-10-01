from django.contrib import admin
from .models import About, Logo, Contact, Our_Team
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'subject', 'message')
   
    readonly_fields = ('full_name', 'email', 'phone_number', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        """Disable adding new contacts via admin"""
        return False

    def has_change_permission(self, request, obj=None):
        """Disable editing existing messages"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Allow deleting messages"""
        return True
admin.site.register(Logo)
admin.site.register(About)
admin.site.register(Our_Team)
