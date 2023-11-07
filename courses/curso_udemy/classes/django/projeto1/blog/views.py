from django.shortcuts import render
from django.http import HttpResponse


# arquivo com json dos blogs
from blog.data import posts


# Create your views here.


def blog(request):
	print("blog")
 
 
	context = {
		'title_blog': "Este é o título do blog",
		'posts': posts,
		'tipo': 68
	}
 
 
	return render(  # renderiza um arquivo html para a view
		request, "blog.html", context
	)
 
 
def post(request, id):
	print(f"post {id}")
 
	for post in posts:
		if post['id'] == id:
			context = {
				'title': post['title'],
				'body': post['body']
			}
 
 
	return render(  # renderiza um arquivo html para a view
		request, "post.html", context
	)
