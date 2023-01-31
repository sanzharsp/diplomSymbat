from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class User_Admin(UserAdmin):
    model = User
    list_display = ('username', 'is_superuser','is_staff')
    list_filter = ('username', 'is_superuser', 'first_name','last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name','last_name','surname','email',)}),
        ('Права доступа и потверждение', {'fields': ('is_staff','is_superuser')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name','last_name','surname','email',)},
            
        ),
         ('Права доступа и потверждение', {'fields': ('is_staff','is_superuser')}),
    )
    search_fields = ('username',)
    ordering = ('username',)


class Profile_Admin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'nameResidentialComplex','roomNumber')
    list_display = ('user', 'nameResidentialComplex','roomNumber')
    search_fields = ('user', 'nameResidentialComplex','roomNumber')
    ordering = ('user', 'nameResidentialComplex','roomNumber')


admin.site.register(User,User_Admin)

admin.site.register(Profile,Profile_Admin)