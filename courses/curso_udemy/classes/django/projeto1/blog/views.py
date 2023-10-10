from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog(request):
	print("home")
	return render(  # renderiza um arquivo html para a view
		request, "blog.html"
	)
