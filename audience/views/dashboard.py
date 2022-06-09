from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from users.models import (
    ADMIN_ROLE,
    STAFF_ROLE,
    CUSTOMER_ROLE
)
from lab.models import Course, Category


class HomeView(TemplateView):
    template_name = 'audience/home.html'


class DashboardView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context.update({
            'dashboard_view': True,
            'courses': courses,
        })
        return context


class AnonymousDashboard(DashboardView):
    template_name = 'audience/anonymous/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        email = self.request.GET.get("email")
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        category1 = Category.objects.get(id=1)
        category2 = Category.objects.get(id=2)
        courses1 = Course.objects.filter(
            category=category1)
        courses2 = Course.objects.filter(
            category=category2)

        context.update({
            'dashboard_view': True,
            'category1': category1,
            'category2': category2,
            'courses1': courses1,
            'courses2': courses2,
        })
        return context


class AdminDashboardView(DashboardView):
    # Change this to admin dashboard/homepage
    template_name = 'audience/admin/dashboard.html'
    # template_name = 'audience/admin/lab_course_create.html'


class StaffDashboardView(DashboardView):
    template_name = 'audience/staff/dashboard.html'


class CustomerDashboardView(DashboardView):
    template_name = 'audience/customer/dashboard.html'


def dashboard_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return AnonymousDashboard.as_view()(request, *args, **kwargs)
    else:
        if request.user.profile.role_id == ADMIN_ROLE:
            return AdminDashboardView.as_view()(request, *args, **kwargs)
        elif request.user.profile.role_id == STAFF_ROLE:
            return StaffDashboardView.as_view()(request, *args, **kwargs)
        elif request.user.profile.role_id == CUSTOMER_ROLE:
            return CustomerDashboardView.as_view()(request, *args, **kwargs)

    return HomeView.as_view()(request, *args, **kwargs)
