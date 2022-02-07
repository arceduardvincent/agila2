import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from lab.models import Course
from audience.forms import CreateCourseForm


class CourseContentView(DetailView):
    template_name = 'audience/customer/course_detail.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        course = Course.objects.get(pk=pk)
        context = {'course': course}
        return render(request, self.template_name, context)


class CreateCourseView(CreateView):
    template_name = 'audience/admin/course_create.html'
    form_class = CreateCourseForm
    success_url = reverse_lazy('audience:audience-dashboard')
