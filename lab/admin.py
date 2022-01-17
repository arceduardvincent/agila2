from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'difficulty', 'category',
                    'created', 'modified',)
    search_fields = ('title',)

    class Media:
        js = [
            'tinymce/jquery.tinymce.min.js',
            'tinymce/tinymce.min.js',
            'js/tinymce/js/textareas.js'
        ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified',)


@admin.register(models.Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified',)
