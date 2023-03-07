from django.contrib import admin
from administration.models import ContactUs, About, Gallery, Item, OpeningHours, Staff, Testimonials


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'created_at']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "created_at"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]\

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]


@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ["id", 'day', 'time', "created_at"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
