# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')


admin.site.register(Contact, ContactAdmin)