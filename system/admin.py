from django.contrib import admin
from system.models import ConfigCategory, ConfigChoice


# Register your models here.
@admin.register(ConfigCategory)
class ConfigCategory(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ConfigChoice)
class ConfigChoice(admin.ModelAdmin):
    list_display = ['id', 'category', 'name']
    list_filter = ['category']
