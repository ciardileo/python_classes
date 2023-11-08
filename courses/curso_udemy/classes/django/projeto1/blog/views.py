from django.shortcuts import render
from django.http import HttpResponse, Http404


# arquivo com json dos blogs
from blog.data import posts


# Create your views here.


def blog(request):
	print("blog")
 
 
	context = {
		'title_blog': "Este é o título do blog",
		'posts': posts,
		'tipo': 1
	}
 
 
	return render(  # renderiza um arquivo html para a view
		request, "blog.html", context
	)
 
 
def post(request, id):
	print(f"post {id}")
	found = False
 
	for post in posts:
		if post['id'] == id:
			found = True
			context = {
				'title': post['title'],
				'body': post['body']
			}
			break


	if not found:
		raise Http404("Este post não existe!")
 
 
	return render(  # renderiza um arquivo html para a view
		request, "post.html", context
	)
