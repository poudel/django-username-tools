from django.contrib import admin
from username_tools.models import UsernameBlacklist


@admin.register(UsernameBlacklist)
class UsernameBlacklistAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_blocked')
    list_filter = ('is_blocked',)
