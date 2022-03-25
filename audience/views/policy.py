from django.views.generic import TemplateView
from django.urls import reverse

class PrivacyPolicyView(TemplateView):
    template_name = 'audience/policy/privacy_policy.html'
    
class TermsUseView(TemplateView):
    template_name = 'audience/policy/terms_use.html'