from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class UserCheckMixin(object):
    user_check_failure_path = reverse_lazy('audience-dashboard')
    user_check_organizatin_id = None

    def check_user(self, user):
        user_role_checked = self.check_user_role(user)
        return user_role_checked

    def check_user_role(self, user):
        return True

    def user_check_failed(self, request, *args, **kwargs):
        return redirect(self.user_check_failure_path)

    def dispatch(self, request, *args, **kwargs):
        if not self.check_user(request.user):
            return self.user_check_failed(request, *args, **kwargs)

        return super(UserCheckMixin, self).dispatch(request, *args, **kwargs)

