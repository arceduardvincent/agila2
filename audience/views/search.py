from django.views.generic import TemplateView, ListView, View
from django.urls import reverse
from django.http import HttpResponse
from lab.models import Course
from django.shortcuts import render

class SearchView(View):
    template_name = 'audience/search.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        result = Course.objects.filter(title=search)
        context = {
            'result': result,
            'search': search
        }
        return render(self.request, self.template_name, context)