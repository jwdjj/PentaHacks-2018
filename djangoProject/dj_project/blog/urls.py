from django.urls import path

#let's import views.py (since this is not java)
from . import views

'''
This is blog app
this urls.py is the route/path management for blog app

You need to route the entire website to this app (the main urls.py)
'''

'''
	It doesn't exactly match the path?
	But it appends to what is given from include()
'''


urlpatterns = [
	path('', views.home, name='blog-home'),
	#empty path == home
	#views.home is home() from views, ret HttpResponse
	#(name don't be too generic for reverse lookup)
	#e.g another app (store) would also have 'home'
	
	#path('',views.about, name='blog-about')
	#^^^ if you have 2 same path (blanks) the first one will execute
	path('about/',views.about, name='blog-about')
	#but because I'm passing it here it can call both blog home and about us
	#don't route from the main url 
	#main -> blog then blog -> blank=home, about=aboutus

]