from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'name', 'isPremiumUser', 'is_active', 'date_joined']
    list_filter = ['isPremiumUser', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'name']
    ordering = ['email']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('name',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Configuración Premium', {'fields': ('isPremiumUser',)}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'isPremiumUser'),
        }),
    )
    
    readonly_fields = ['date_joined', 'last_login']
