from django.contrib import admin

from .models import Department, Position, CustomUser
from django.contrib.auth.admin import UserAdmin


# -------------------- Department --------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'unit_type', 'level', 'parent', 'is_sovereign')
    list_filter = ('unit_type', 'level', 'is_sovereign')
    search_fields = ('name', 'code')
    ordering = ('level', 'name')


# -------------------- Position --------------------
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'rank', 'can_approve')
    list_filter = ('department', 'can_approve')
    search_fields = ('title',)
    ordering = ('department', 'rank')


# -------------------- Custom User --------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'first_name', 'last_name', 'department', 'position', 'is_staff')
    list_filter = ('department', 'position', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {
            'fields': ('department', 'position', 'job_title', 'phone_number', 'signature_image')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('معلومات إضافية', {
            'fields': ('department', 'position', 'job_title', 'phone_number', 'signature_image')
        }),
    )

    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)
# Register your models here.
