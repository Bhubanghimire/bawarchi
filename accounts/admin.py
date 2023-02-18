from django.contrib import admin
from accounts.models import User


# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
