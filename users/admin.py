from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from . import models

User = get_user_model()

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'birth_date', 'address',
                    'phone', 'gender', 'is_active', 'created', 'modified',)
    raw_id_fields = ("user",)
    list_filter = ('role', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email',
                     'user__username', 'address',)


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
