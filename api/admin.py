from django.contrib import admin
from .models import User, Message

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'email']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
 list_display = ['id', 'message', 'created_on', 'updated_on','created_by']