"""
URL configuration for DJANGOAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLcnf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.home.home_views import home_views
from api.login.login_view  import (
    login_views, register_view,
    forgot_view, logout_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views, name='login'),
    path('register/', register_view, name='register'),
    path('forgot/', forgot_view, name='forgot'),
    path('logout/', logout_view, name='logout'),
    path('', home_views, name='home'),  # Ruta raíz
]

