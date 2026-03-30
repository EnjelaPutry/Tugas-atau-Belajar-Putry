from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("<h1>This is the about page.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index, name='index'),
    path('about/', about, name='about'),
]
