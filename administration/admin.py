from django.contrib import admin
from administration.models import ContactUs


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'created_at']
