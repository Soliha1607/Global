from django.contrib import admin

# Register your models here.

from .models import Work,  About, Contact


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
   list_display = ['title', 'description']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['address', 'email', 'phone']