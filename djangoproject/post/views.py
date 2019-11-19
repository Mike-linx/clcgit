from django.shortcuts import render

from .models import post as Post

# Create your views here.
def index(request):
	
	post = Post.objects.all()

	print(post)


	context ={
		'post':post
	}

	return render(request, 'post/index.html', context)


def detail_post(request, post_id):
	Templates = 'post/detail_post.html'
	post = Post.objects.get(id=post_id)
	context = {"post": post}
	return render(request, Templates, context)

#this anre
