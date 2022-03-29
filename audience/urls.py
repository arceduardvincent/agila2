from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = "audience"
urlpatterns = [
    # COMMON PAGES
    url(r'^$', dashboard_view, name='dashboard'),
    path('privacy_policy', PrivacyPolicyView.as_view(), 
        name='privacy_policy'),
    path('terms_use', PrivacyPolicyView.as_view(), 
        name='terms_use'),
    url(r'^course/detail/(?P<pk>\d+)/$', CourseContentView.as_view(),
        name='course-content-view'),
    url(r'^lab/course/create/$', login_required(CreateCourseView.as_view()),
        name='audience-course-create'),
    url(r'^lab/course/edit/(?P<pk>\d+)/$', login_required(ModifyCourseView.as_view()),
        name='audience-course-edit'),
    url(r'^lab/track/create/$', login_required(LabTrackView.as_view()),
        name='audience-lab-track-create'),
]