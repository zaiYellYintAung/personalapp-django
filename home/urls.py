from django.urls import path
from . import views

urlpatterns=[
	path('',views.root,name="root"),
	path('about/',views.about,name="about"),
]