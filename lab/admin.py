from django.contrib import admin

from . import models


class ChoiceInline(admin.StackedInline):
    extra = 0
    fieldsets = (
        ("Choices", {
            'fields': (
                ('question', 'choice_desc'),
            ),
        }),

    )
    model = models.Choice


class QuestionInline(admin.StackedInline):
    extra = 0
    fieldsets = (
        ("Choices", {
            'fields': (
                ('title', 'type_question'),
            ),
        }),

    )
    model = models.Question


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'difficulty',
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


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_question', 'created', 'modified')
    inlines = (ChoiceInline,)
    save_on_top = True


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created', 'modified')
    inlines = (QuestionInline,)
    save_on_top = True


@admin.register(models.SubscriberStatus)
class SubscriberStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'course', 'created', 'modified')
    save_on_top = True


@admin.register(models.SubscriberChoice)
class SubscriberChoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'choice', 'created', 'modified')
    save_on_top = True


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_desc', 'created', 'modified')
    save_on_top = True
