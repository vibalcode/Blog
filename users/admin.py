from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login']
    # list_display_links = ['id', 'username', 'email']
    # list_filter = ['is_staff', 'is_superuser', 'is_active']
    # search_fields = ['username', 'email', 'first_name', 'last_name']
    # list_per_page = 25
    # ordering = ['id']
    # readonly_fields = ['date_joined', 'last_login']
    # fieldsets = [
    #     ('User Information', {'fields': ['username', 'email', 'first_name', 'last_name']}),
    #     ('Permissions', {'fields': ['is_staff', 'is_superuser', 'is_active']}),
    #     ('Important Dates', {'fields': ['date_joined', 'last_login']}),
    # ]
    # add_fieldsets = [
    #     ('User Information', {'fields': ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']}),
    #     ('Permissions', {'fields': ['is_staff', 'is_superuser', 'is_active']}),
    # ]
    pass