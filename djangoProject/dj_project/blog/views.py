from django.shortcuts import render
#from django.http import HttpResponse

posts2 = [
	{
		'author': 'moi',
		'title' : 'post1',
		'content' : 'FIRST!!',
		'date' : 'November 18 2018' #screw time object
	},
	{
		'author': 'shak',
		'title' : 'post2',
		'content' : 'SECOND!!',
		'date' : 'November 19 2018' #screw time object
	}
]

# Create your views here.
# Function HOME handles traffic of homepage
# takes in request argument 
# return what we want user to see when they're sent to this route

def home(request):
	context = {
	'posts' : posts2,
	#'title' : "PHIMS HOME"	
	}
	return render(request,'blog/home.html',context)
# need to map url pattern to this function in views.py
# create a bot module in blog dir (urls.py) 
# ^file we map each url to each 'views.py' function

def about(request):
	return render(request,'blog/about.html')

