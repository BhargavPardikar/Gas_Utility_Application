from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ('id', 'request_type', 'status', 'submitted_at', 'resolved_at')
    
    # Fields that can be edited directly in the list view
    list_editable = ('status', 'resolved_at')
    
    # Add filters for status and request type
    list_filter = ('status', 'request_type')
    
    # Add a search bar to search by details or customer name (if applicable)
    search_fields = ('details',)
    
    # Enable pagination
    list_per_page = 20
