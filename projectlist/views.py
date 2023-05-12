from django.shortcuts import render

# Create your views here.
def projects(request):
	template="projectlist/projects.html"
	data={}
	return render(request,template,data)