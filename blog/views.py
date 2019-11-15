from django.shortcuts import render
from .models import Blog, Comment

def homepage(request):
	# select * from blog;
	blogs = Blog.objects.all()
	return render(request, 'blog/home.html', {"ourblogs": blogs})


def detail_post(request, blog_id):
	template = 'blog/detail_blog.html'
	blog = Blog.objects.get(id=blog_id)
	context = {"blog": blog}
	return render(request, template, context)
 