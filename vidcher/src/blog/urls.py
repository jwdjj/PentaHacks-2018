from django.urls import path

from . import views


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('submission/', views.submission, name='blog-submission'),
	path('login/', views.login, name='blog-login'),
	path('dashboard/', views.dashboard, name='blog-dashboard'),
	path('data/', views.data, name='blog-data'),
	path('settings/', views.settings, name='blog-settings'),
]