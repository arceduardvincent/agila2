from django.db import models
from generic.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models


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
    title = models.CharField(_('Name'), max_length=250)
    difficulty = models.ForeignKey(
        'lab.Difficulty',
        verbose_name=_('Difficulty'),
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'lab.Category',
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    content = tinymce_models.HTMLField()
    instructor = models.ForeignKey(
        'users.Instructor',
        verbose_name=_('Instructor'),
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

