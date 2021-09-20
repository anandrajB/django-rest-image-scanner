"""scanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetConfirmView , PasswordResetCompleteView
from django.contrib.auth import views as auth_views
# from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pass/', include('django.contrib.auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth',include('rest_framework.urls')),
    path('scanner/', include('accounts.urls')),
    path('rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registrations/password_reset_form.html'),
    #      name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views. PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('reset/done/', auth_views. PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
    #      name='password_reset_complete'),