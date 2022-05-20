from django.views.generic import TemplateView, ListView, View
from django.urls import reverse
from django.http import HttpResponse
from lab.models import Course
from django.shortcuts import render

class Search(View):
    template_name = 'audience/search.html'

    def get(self, request, *args, **kwargs):
        get_data = request.GET.get('search')
        result = Course.objects.filter(title=get_data)
        context = {
            'result': result
        }
        return render(self.request, self.template_name, context)