from django.views.generic import TemplateView

class PrivacyView(TemplateView):
    template_name = 'audience/anonymous/dashboard.html'