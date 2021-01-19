""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from insta.views import registerPage, loginPage, show_post
from django.contrib.auth import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register', registerPage, name='register'),
    url(r'^login', loginPage, name='login'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url('', include('insta.urls') ), 
    url(r'^profile', include('insta.urls')),
    url(r'^upload', include('insta.urls')),
    url(r'^post/(\d)/', include('insta.urls')),
]
