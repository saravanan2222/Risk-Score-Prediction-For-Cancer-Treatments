"""
URL configuration for riskscoreofcancer project.

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

# urls.py
# from django.contrib import admin
# from django.urls import path
# from django.views.generic.base import RedirectView
# from riskscoreapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('password-login/', views.password_login, name='password_login'), 
#     path('logout/', views.custom_logout_view, name='logout'),
#     path('home/', views.home, name='home'),  # Home page
#     path('insert/', views.insert_view),
#     path('insert/home.html', views.home),
#     path('display/', views.display_view),
#     path('update/', views.update1_view),
#     path('update/<int:id>/', views.update_view),
#     path('search/', views.search_view),
#     path('delete/', views.delete_view),
#     path('delete/home.html', views.home),
#     path('search/home.html', views.home),
#     path('display/home.html', views.home),
#     path('insert/home.html', views.home),
#     path('update/home.html', views.home),
#     path('update/<int:id>/home.html', views.home)
#     path('', RedirectView.as_view(url='/password-login/', permanent=False))
# ]
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView  # Import RedirectView

from riskscoreapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-login/', views.password_login, name='password_login'), 
    path('logout/', views.custom_logout_view, name='logout'),
    path('home/', views.home, name='home'),  # Home page
    path('insert/', views.insert_view),
    path('insert/home.html', views.home),
    path('display/', views.display_view),
    path('update/', views.update1_view),
    path('update/<int:id>/', views.update_view),
    path('search/', views.search_view),
    path('delete/', views.delete_view),
    path('delete/home.html', views.home),
    path('search/home.html', views.home),
    path('display/home.html', views.home),
    path('insert/home.html', views.home),
    path('update/home.html', views.home),
    path('update/<int:id>/home.html', views.home),
    path('', RedirectView.as_view(url='/password-login/', permanent=False))  # Redirect root URL to /password-login/
]