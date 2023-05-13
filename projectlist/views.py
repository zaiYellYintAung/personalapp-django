from django.shortcuts import render
from .models import *
# Create your views here.
def projects(request):
	template="projectlist/projects.html"
	projects=Projects.objects.all()
	data={
		'projects':projects
	}
	return render(request,template,data)


def project(request,pk):
	template="projectlist/project.html"
	project=Projects.objects.get(id=pk)

	data={
		'project':project
	}
	return render(request,template,data)

def create(request):
	template="projectlist/form.html"
	data={}
	return render(request,template,data)

