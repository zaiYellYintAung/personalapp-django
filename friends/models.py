from django.db import models

# Create your models here.
class Relations(models.Model):
	name=models.CharField(max_length=69)

	def __str__(self):
		return f"{self.name}"

class Friends(models.Model):
	name=models.CharField(max_length=69)
	relation=models.ForeignKey(Relations,on_delete=models.CASCADE,related_name="relationsx")
	profilelink=models.URLField(blank=True,null=True)
	email=models.EmailField(blank=True, null=True)
	description=models.TextField(blank=True,null=True)

	def __str__(self):
		return f"{self.name}"