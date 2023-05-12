from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def begeni(request):
    return render(request, 'begenilerim.html')

def detail(request):
    return render(request, 'detail.html')

def icerik(request):
    return render(request, 'icerik.html')

def post(request):
    return render(request, 'post.html')

