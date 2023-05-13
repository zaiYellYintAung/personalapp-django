from django.shortcuts import render,redirect
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

	if request.method=='POST':
		form=BlogForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('blogs')

	data={
		'blog_form':blog_form
	}
	return render(request,template,data)

def edit(request,pk):
	template="blogs/edit.html"
	blog_form=BlogForm()

	if request.method=='POST':
		form=BlogForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('blogs')

	data={
		'blog_form':blog_form
	}
	return render(request,template,data)

def show(request,pk):
	template="blogs/blog-detail.html"
	blog=Blogs.objects.get(id=pk)

	data={
		'blog':blog
	}
	return render(request,template,data)
	
