from django.db import models


# Create your models here.

class Topic(models.Model):
	name=models.CharField(max_length=69)

	def __str__(self):
		return f"{self.name}"


class Blogs(models.Model):
	title=models.CharField(max_length=69)
	body=models.TextField()
	topic=models.ManyToManyField(Topic)
	created=models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title}"


