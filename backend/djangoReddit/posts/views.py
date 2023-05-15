
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'index.html',context)

from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from user.forms import *

# Create your views here.
def index(request):
    username = ''
    email = ''
    password1 = ''
    password2 = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı kullanılıyor.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Bu email zaten alinmis.')    
            elif len(password1) < 8:
                messages.error(request, 'Parola en az 8 karakter olmali.')  
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Basariyla kayit oldunuz.')   
                return redirect('index')   
        else:
            messages.error(request, 'Parolalar eslesmiyor.')    
    context = {
        'username': username,
        'email': email,
        'password1': password1,
        'password2': password2,
    }
    return render(request, 'index.html' , context)


def begeni(request):
    return render(request, 'begenilerim.html')

def detail(request):
    return render(request, 'detail.html')

def icerik(request):
    return render(request, 'icerik.html')

def post(request):
    return render(request, 'post.html')

