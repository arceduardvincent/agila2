from django.db import models
from generic.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models
from users.models import User
from model_utils import Choices
from generic.constants import image_file_path

BEGINNER = 1  # Actual ID


class Difficulty(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    description = models.CharField(
        _('Description'),
        max_length=512, blank=True
    )

    class Meta:
        verbose_name_plural = "Difficulties"

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    description = models.CharField(
        _('Description'),
        max_length=512, blank=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(BaseModel):
    code = models.CharField(_('Code'), max_length=250)
    banner = models.ImageField(
        _('Course Banner'),
        upload_to=image_file_path,
        blank=True,
        null=True
    )
    title = models.CharField(_('Title'), max_length=250)
    overview = tinymce_models.HTMLField(_('Overview'), null=True)
    objective = tinymce_models.HTMLField(_('Objective'), null=True)
    prerequisites = tinymce_models.HTMLField(_('Prerequisites'), null=True)
    content = tinymce_models.HTMLField(_('Content'), null=True)
    difficulty = models.ForeignKey(
        'lab.Difficulty',
        verbose_name=_('Difficulty'),
        on_delete=models.CASCADE,
        default=BEGINNER

    )
    instructor = models.ForeignKey(
        'users.Instructor',
        verbose_name=_('Instructor'),
        on_delete=models.CASCADE,
        null=True,
    )
    category = models.ForeignKey(
        'lab.Category',
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)  # Flag if the course is published.
    # Lets assume on the future that we need to check the total subscriber
    # who take the course.
    progress_percentage = models.FloatField(default=0)
    point = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

    def get_lessons(self):
        lessons = Lesson.objects.filter(course=self)
        return lessons


class OperatingSystem(BaseModel):
    image = models.ImageField(
        _('Image'),
        upload_to=image_file_path,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255,  null=True)
    is_active = models.BooleanField(default=True)


class OSTemplate(BaseModel):
    image = models.ImageField(
        _('Image'),
        upload_to=image_file_path,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255,  null=True)
    is_active = models.BooleanField(default=True)


class LabProfile(BaseModel):
    course = models.ForeignKey(
        Course, null=True, related_name="course_lab_profile",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        _('Image'),
        upload_to=image_file_path,
        blank=True,
        null=True
    )
    title = models.CharField(max_length=255,  null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    course = models.ForeignKey(
        Course, null=True, related_name="course",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255,  null=True)
    content = tinymce_models.HTMLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(BaseModel):
    TYPE_QUESTION = Choices(
        'Text', 'Rating', 'Yes or No', 'Multiple Choice',
        'Integer', 'Multiple Select'
    )
    lesson = models.ForeignKey(
        Lesson, null=True,
        related_name="lesson",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    type_question = models.CharField(
        max_length=255, choices=TYPE_QUESTION,
        default='Multiple Choice'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_desc = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.question, self.choice_desc)


class SubscriberChoice(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.choice)

    class Meta:
        verbose_name = "SubscriberChoice"
        verbose_name_plural = "SubscriberChoice"
        ordering = ['-created']


class SubscriberCourseStatus(BaseModel):
    STATUS = Choices('Complete', 'Incomplete')
    status = models.CharField(max_length=255, choices=STATUS,
                              default=STATUS.Incomplete)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "SubscriberCourseStatus"
        verbose_name_plural = "SubscriberCourseStatuses"
        ordering = ['-created']

