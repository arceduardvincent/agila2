from django.views.generic import TemplateView
from users.models import (
    ADMIN_ROLE,
    STAFF_ROLE,
    CUSTOMER_ROLE
)


class HomeView(TemplateView):
    template_name = 'audience/home.html'


class DashboardView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update({'dashboard_view': True})
        return context


class AnonymousDashboard(DashboardView):
    template_name = 'audience/anonymous/dashboard.html'


class AdminDashboardView(DashboardView):
    template_name = 'audience/admin/dashboard.html'


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