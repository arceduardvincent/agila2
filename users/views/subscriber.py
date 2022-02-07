from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from users.forms.subscriber import SubscriberSignupForm


class SubscriberSignupView(FormView):
    template_name = 'users/auth/signup.html'

    form_class = SubscriberSignupForm
    success_url = reverse_lazy('users-login')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'])
        user.profile.role_id = 3
        user.save()
        return HttpResponseRedirect(self.get_success_url())
