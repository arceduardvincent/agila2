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
        ("Questions", {
            'fields': (
                ('title', 'content', 'type_question'),
            ),
        }),

    )
    model = models.Question


class LessonInline(admin.StackedInline):
    extra = 0
    fieldsets = (
        ("Lessons", {
            'fields': (
                ('title', 'course', 'content', 'is_active'),
            ),
        }),

    )
    model = models.Lesson


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'difficulty',  'is_active',
                    'created', 'modified',)
    search_fields = ('title',)
    inlines = (LessonInline,)

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
    list_display = ('title', 'type_question',  'is_active',
                    'created', 'modified')
    inlines = (ChoiceInline,)
    save_on_top = True


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',  'is_active', 'created', 'modified')
    inlines = (QuestionInline,)
    save_on_top = True


@admin.register(models.SubscriberCourseStatus)
class SubscriberCourseStatusAdmin(admin.ModelAdmin):
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
