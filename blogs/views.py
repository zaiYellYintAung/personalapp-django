from django.shortcuts import render
from .models import Blogs
from .forms import BlogForm

# Create your views here.
def blogs(request):
	template="blogs/index.html"
	blogs=Blogs.objects.all()

	data={
		"blogs":blogs
	}
	return render(request,template,data)

def create(request):
	template="blogs/create.html"
	blog_form=BlogForm()

	data={
		'blog_form':blog_form
	}
	return render(request,template,data)

