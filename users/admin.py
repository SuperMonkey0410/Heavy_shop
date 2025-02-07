from django.contrib import admin
from users.models import User

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'last_login',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
