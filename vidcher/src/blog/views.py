from django.shortcuts import render

mockData = [
		{
			'name': 'Jessica',
			'FileName' : 'Jess.csv',
			'date' : 'November 18 2018'
		},
		{
			'name': 'Naida Tania',
			'FileName' : 'NaidaIsAwesome.csv',
			'date' : 'November 19 2018'
		}
]

context = {
	'posts' : mockData,
}

def home(request):
	return render(request,'blog/home.html')

def submission(request):
	return render(request,'blog/submission.html')

def login(request):
	return render(request,'blog/login.html')

def dashboard(request):
	return render(request,'blog/dashboard.html', context)

def data(request):
	return render(request,'blog/data.html', context)

def settings(request):
	return render(request,'blog/settings.html')

