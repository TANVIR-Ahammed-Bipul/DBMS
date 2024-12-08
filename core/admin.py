from django.contrib import admin
from django.db.models import Sum
from django.urls import path
from django.shortcuts import render
from .models import File, DataItem
from django.contrib.admin import AdminSite

# ModelAdmin for File
class FileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'user', 'upload_date', 'file']
    search_fields = ['file_name', 'user__username']
    list_filter = ['upload_date', 'user']

# ModelAdmin for DataItem
class DataItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'user__username']
    list_filter = ['created_at', 'updated_at', 'user']

# Custom Admin Site
class CustomAdminSite(AdminSite):
    site_header = "Datavault Admin Panel"
    site_title = "Datavault Admin"
    index_title = "Welcome to Datavault Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('aggregates/', self.admin_view(self.aggregate_view), name="aggregate_view"),
        ]
        return custom_urls + urls

    def aggregate_view(self, request):
        total_uploads = File.objects.aggregate(Sum('file_size'))
        return render(request, 'admin/aggregates.html', {'total_uploads': total_uploads})

# Register models with the custom admin site
admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(File, FileAdmin)
admin_site.register(DataItem, DataItemAdmin)
