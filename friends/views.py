from django.shortcuts import render

# Create your views here.
def friends(request):
	template="friends/index.html"

	data={}
	return render(request,template,data)
