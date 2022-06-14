from django.conf.urls import url, include
from django.urls import path, reverse
from django.contrib.auth.decorators import login_required
from .views import *

app_name = "audience"
urlpatterns = [
    # COMMON PAGES
    url(r'^$', dashboard_view, name='dashboard'),
    path('privacy_policy', PrivacyPolicyView.as_view(), 
         name='privacy_policy'),
    path('search', SearchView.as_view(), name='search'),
    path('checkout', login_required(CheckoutView.as_view()), name='checkout'),
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
    url(r'^course/gradebook/$', login_required(
        SubscriberGradeBookList.as_view()), name='course-gradebook-view'),
    path('order/<int:id>', OrderView.as_view(), name='order_item'),
    path('order/<int:id>/remove', RemoveOrderView.as_view(),
         name='delete_item'),
]

