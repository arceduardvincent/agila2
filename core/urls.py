"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from lab import views


admin.site.site_header = "Agila Marketplace Admin"
admin.site.index_title = "Welcome to Agila Marketplace"
admin.site.site_title = "Agila Marketplace"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('users.urls')),
    path('api/users/', include('api.v1.users.urls')),
    path('upload_image/', views.upload_image),
    path('tinymce/', include('tinymce.urls')),
    path('', include('audience.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# swagger
api_info = openapi.Info(
    title="Agila API",
    default_version="v1",
    description="API documentation for Red Sound App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
