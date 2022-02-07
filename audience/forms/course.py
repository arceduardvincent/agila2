from datetime import date, datetime, timedelta, time
import logging

from django import forms
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.forms import formset_factory, modelformset_factory
from django.utils.translation import ugettext_lazy as _
from lab.models import Course


class CreateCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('code', 'title', 'difficulty', 'content', 'instructor', 'is_active')
