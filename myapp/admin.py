from django.contrib import admin

# Register your models here.

from.models import client_msg


class client_msgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')  # Display these fields in the admin list view
    search_fields = ('name', 'email', 'phone')  # Enable search by name, email, and phone
    list_filter = ('name',)  # Add a filter sidebar for the name field
admin.site.register(client_msg, client_msgAdmin)