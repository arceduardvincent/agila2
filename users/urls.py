from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import SubscriberSignupView

urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(
        template_name='users/auth/login.html',
        redirect_authenticated_user=True),
        name='users-login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(
        next_page='/'),
        name='users-logout'),
    url(r'^signup/$', SubscriberSignupView.as_view(),
        name='user-subscriber-signup'),
]