from django.views.generic import TemplateView, ListView, View
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render

from lab.models import Course, Category


class SearchView(View):
    template_name = 'audience/search.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        result = Course.objects.filter(title__icontains=search)
        category = Category.objects.get(id=2)
        courses = Course.objects.filter(category=category)
        context = {
            'result': result,
            'search': search,
            'courses': courses,
            'category': category
        }
        return render(self.request, self.template_name, context)