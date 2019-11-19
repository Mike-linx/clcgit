from django.db import models

class Blog(models.Model):
	title = 	models.CharField(max_length=50)
	body = 		models.TextField()
	author = 	models.CharField(max_length=30)
	timestamp = models.DateTimeField(auto_now_add=True)
	picture = 	models.ImageField(upload_to="media/", blank=True, null=True)
	likes = 	models.IntegerField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	commenter = models.CharField(max_length=20)
	comment = 	models.CharField(max_length=150)
	post =	  	models.ForeignKey(Blog, on_delete=models.CASCADE)
	posted = 	models.DateTimeField(auto_now_add=True)
	no_likes = 	models.IntegerField(default=0)



	def __str__(self):
		return self.comment