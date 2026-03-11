from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')

# forma de desregistrar el modelo User
admin.site.unregister(User)
admin.site.register(User, CustomAdmin)
