from django.contrib import admin
from .models import Address, User, Profile
from .forms import UserForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Address)
admin.site.register(Profile)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserForm

    list_display = ('username', 'phone', 'is_staff')
    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'phone')}),
        ('Permissions', {'classes': ('collapse',), 'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Group Permissions', {'classes': ('collapse',), 'fields': ('groups', 'user_permissions',)})
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'phone')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    search_fields = ('username',)
    ordering = ('is_staff',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
