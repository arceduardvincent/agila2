from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'rating', 'created', 'modified')
