from django.shortcuts import render
from .models import Post

# Create your views here.
# this is the logic to handle certain routes

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 

