from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'index.html',context)

def begeni(request):
    return render(request, 'begenilerim.html')

def detail(request):
    return render(request, 'detail.html')

def icerik(request):
    return render(request, 'icerik.html')

def post(request):
    return render(request, 'post.html')

