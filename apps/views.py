from django.shortcuts import render

# Create your views here.
def apps(request):
	template="apps/index.html"

	data={}
	return render(request,template,data)
