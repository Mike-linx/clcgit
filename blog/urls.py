from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="homepage"),
	path('<int:blog_id>/', views.detail_post, name="detail"),
	path('post/comment', views.post_comment, name="post_comment"),
]