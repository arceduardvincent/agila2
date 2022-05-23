from django.views.generic import TemplateView, ListView, View
from django.urls import reverse
from django.http import HttpResponse
from lab.models import Course
from django.shortcuts import render


class CheckoutView(View):
    template_name = 'audience/checkout.html'

    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(self.request, self.template_name, context)