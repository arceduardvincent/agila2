from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import *

app_name = "audience"
urlpatterns = [
    # COMMON PAGES
    url(r'^$', dashboard_view, name='audience-dashboard'),
    url(r'^course/detail/(?P<pk>\d+)/$', CourseContentView.as_view(),
        name='course-content-view'),
    url(r'^course/create/$', login_required(CreateCourseView.as_view()),
        name='audience-course-create'),
    url(r'^lab/track/(?P<pk>\d+)$', LabtrackView.as_view(),
        name='audience-lab-track'),
]