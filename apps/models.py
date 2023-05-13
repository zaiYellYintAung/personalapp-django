from django.db import models

# Create your models here.
class Blogs(models.Model):
	title=models.CharField(max_length=69)
	boby=models.TextField()
	created=models.DateTimeField(auto_created=True)