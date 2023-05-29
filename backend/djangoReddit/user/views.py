from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import *
from posts.models import *

# Create your views here.
def giris(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username = username , password = password)



        if user is not None:
            login(request , user)
            
            messages.success(request , 'Giris Yapildi')
            return redirect('index')
        else:
            messages.info(request , 'Kullanıcı Adı veya Parola Hatalı')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def cikis(request):
    logout(request)
    messages.success(request , 'Çıkıs Yapıldı')
    return redirect('index')    

def profilayarlar(request):
    return render(request, 'settingsProfil.html')

def genelayarlar(request):
    return render(request, 'UserSettings.html')

def profil(request,profilId):
    posts=Post.objects.all()
    topluluk = User.objects.get(id=profilId)
    posts1 = Post.objects.filter(yazar_id=topluluk  )
    context = {
        'topluluk': topluluk,
        'posts1': posts1,
        'posts': posts
    } 
    return render(request , 'profil.html',context)