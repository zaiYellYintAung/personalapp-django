from django.shortcuts import render

# Create your views here.
def root(request):
	template="home/root.html"

	data={}
	return render(request,template,data)

def about(request):
	template="home/about.html"

	data={}
	return render(request,template,data)