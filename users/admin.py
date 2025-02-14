from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "username", "choice", "date_joined"
    list_filter = ("choice",)
