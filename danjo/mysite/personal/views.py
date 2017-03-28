from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')
def contact(request):
	return render(request,'personal/basic.html', {'content':['If you like to contact me ,mail me or call me','rohangho@live.com','9051810270']})
