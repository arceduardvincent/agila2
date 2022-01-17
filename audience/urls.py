from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # COMMON PAGES
    url(r'^$', login_required(dashboard_view), name='audience-dashboard'),
]