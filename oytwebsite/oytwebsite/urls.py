"""
URL configuration for oytwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views as base_views
from user import views as user_views

urlpatterns = [
    path('', base_views.HomeView.as_view(), name='home'),
    path('about/', base_views.AboutView.as_view(), name='about'),
    path('faq/', base_views.FaqView.as_view(), name='faq'),
    path('contact/', base_views.ContactView.as_view(), name='contact'),
    path('arge/', include('arge.urls')),
    path('event/', include('event.urls')),
    path('enroll/', user_views.EnrollView.as_view(), name='enroll'),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
