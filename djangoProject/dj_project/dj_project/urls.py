"""dj_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), #blog.urls is blog.urls.py
    #oh so this include is so that the next page will check a pattern
    #btw w/o trailing slashes blog/about becomes /blogabout/ so there's that
    #in this main folder, if path is empty, it'll become main page
    #(main as in first thing you see when you call server name alone

    #path('',blog.views.actualhome) in hindsight this makes no sense
    #why would you wanna access blog while bypassing blog
 
]
