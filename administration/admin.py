from django.contrib import admin
from administration.models import ContactUs, About


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'created_at']
