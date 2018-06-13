from django.contrib import admin

from .models import Session

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'resource', 'client_id', 'tenant', 'expires_on', 'created_at']
    list_filter = ['expires_on', 'created_at']
    search_fields = ['id', 'tenant', 'resource', 'client_id']


admin.site.register(Session, SessionAdmin)