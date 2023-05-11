from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def begeni(request):
    return render(request, 'begenilerim.html')
