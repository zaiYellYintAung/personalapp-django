from django.shortcuts import render
from .models import Friends
# Create your views here.
def friends(request):
	template="friends/index.html"
	friends=Friends.objects.all()

	data={
		"friends":friends
	}
	return render(request,template,data)
