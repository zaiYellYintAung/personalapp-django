from django.urls import path
from . import views

urlpatterns=[
	path('',views.blogs,name="blogs"),
	path('create-blogs/',views.create,name="create-blog"),
	path('blog/<str:pk>',views.show,name="blog-detail"),
	path('edit-blog/<str:pk>',views.edit,name="edit-blog"),

	]