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
    DetailView,
    TemplateView
)
from django.utils.translation import ugettext_lazy as _
from audience.forms import CreateCourseForm
from lab.models import (
    Course
)


class CourseContentView(DetailView):
    template_name = 'audience/customer/course_detail.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        course = Course.objects.get(pk=pk)
        context = {'course': course}
        return render(request, self.template_name, context)


class CreateCourseView(CreateView):
    template_name = 'audience/admin/lab_course_create.html'
    form_class = CreateCourseForm
    success_url = reverse_lazy('audience:dashboard')

    def get_context_data(self, **kwargs):
        context = super(CreateCourseView, self).get_context_data(**kwargs)
        course = None
        session_course_id = self.request.session.get('course_id', None)
        if session_course_id:
            course = Course.objects.get(id=session_course_id)
        data = {
            'course_is_active': True,
            'course': course
        }
        context.update(data)
        return context


class LabTrackView(FormView):
    template_name = 'audience/admin/lab_track_create.html'
    form_class = CreateCourseForm
    success_url = reverse_lazy('audience:audience-dashboard')

    def get_context_data(self, **kwargs):
        context = super(LabTrackView, self).get_context_data(**kwargs)
        data = {
            'lab_is_active': True
        }
        context.update(data)
        return context


class ModifyCourseView(UpdateView):
    template_name = 'audience/admin/lab_course_create.html'
    form_class = CreateCourseForm
    model = Course
    success_url = reverse_lazy('audience:dashboard')

    def get_object(self, queryset=None):
        course_id = self.kwargs['pk']
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(pk=course_id)

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super(ModifyCourseView, self).get_context_data(**kwargs)
        course = Course.objects.get(id=self.kwargs['pk'])
        data = {
            'course_is_active': True,
            'course': course
        }
        context.update(data)
        return context

    def form_valid(self, form):
        course_id = self.kwargs['pk']
        course = Course.objects.get(pk=course_id)
        course.code = form.cleaned_data['code']
        course.title = form.cleaned_data['title']
        course.overview = form.cleaned_data['overview']
        course.objective = form.cleaned_data['objective']
        course.prerequisites = form.cleaned_data['prerequisites']
        course.content = form.cleaned_data['content']
        course.save()
        return HttpResponseRedirect(self.get_success_url())