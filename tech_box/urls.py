"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path, include, re_path
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
#urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('authentication.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path(r'^i18n/', include('django.conf.urls.i18n')),
    path('setlang/', set_language, name='set_language'),


]


urlpatterns = i18n_patterns(
    path('', include('dashboard.urls')),
    path('', include('authentication.urls')),
    path(r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
