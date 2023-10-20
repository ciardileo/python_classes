from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

context =   {
	  'title_home': "Esta é a página home"
}

def home(request):
	print("home")
	return render(
		request, "home.html", context
	)
