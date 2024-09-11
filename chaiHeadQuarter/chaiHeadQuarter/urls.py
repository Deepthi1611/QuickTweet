"""
URL configuration for chaiHeadQuarter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/',include('tweet.urls')), 
    path('accounts/', include('django.contrib.auth.urls'))
    # All the URLs provided by Django's authentication system will be prefixed with accounts/
    # By adding this line, you are essentially linking the built-in authentication system to your project.
    # This line in urls.py is what actually provides the URL patterns and views for login, logout, password reset, and other authentication features.
    # Without this, Django won’t know where to find the views for logging in or logging out, and you'll get a "Page Not Found (404)" error 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
