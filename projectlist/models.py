from django.db import models
from friends.models import *

# Create your models here.
class Tags(models.Model):
	name=models.CharField(max_length=69)

	def __str__(self):
		return f"{self.name}"

class Projects(models.Model):
	title=models.CharField(max_length=100)
	body=models.TextField()
	links=models.CharField(max_length=500,null=True,blank=True)
	tags=models.ManyToManyField(Tags)
	date=models.DateField()
	contributers=models.ManyToManyField(Friends)