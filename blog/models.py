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
	comment = models.CharField(max_length=150)
	post =	  models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment