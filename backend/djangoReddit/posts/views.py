from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from user.forms import *
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
   


# Create your views here.
def index(request):
    posts=Post.objects.all()
    topplulukadı=Toplulukolusturma.objects.all()
    username = ''
    email = ''
    password1 = ''
    password2 = ''
    if request.method == 'POST':
        if 'register' in request.POST:
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
    if request.method == 'POST':
        if request.user.is_authenticated:
            postId = request.POST['postId']
            post = Post.objects.get(id = postId)
            if 'like' in request.POST:
                if request.user.profile in post.like.all():
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect ('index')
                else:
                    post.like.add(request.user.profile)
                    post.dislike.remove(request.user.profile)
                    post.save()
                    return redirect('index')
            if 'dislike' in request.POST:
                if request.user.profile in post.dislike.all():
                    post.dislike.remove()
                    post.save()
                    return redirect('index')
                else:
                    post.dislike.add(request.user.profile)
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect('index')     
    context = {
        'username': username,
        'email': email,
        'password1': password1,
        'password2': password2,
        'posts':posts,
        'topplulukadı':topplulukadı
    }
    return render(request, 'index.html' , context)


def begeni(request):
    return render(request, 'begenilerim.html')

def detail(request,postId):
    posts=Post.objects.get(id=postId)
    posts1=Post.objects.all()
    context = {
        'posts':posts,
        'posts1':posts1
    }
    return render(request, 'detail.html',context)

def icerik(request, toplulukId):
    topluluk = Toplulukolusturma.objects.get(id=toplulukId)
    posts1 = Post.objects.filter(grup_id=topluluk)
    context = {
        'topluluk': topluluk,
        'posts1': posts1,
    } 

    return render(request, 'icerik.html', context)



@login_required(login_url='login')
def post(request):
    topplulukadı=Toplulukolusturma.objects.all()

    postcontent = ''
    postimg= ''
    grup=''
    #sayfada çalıştırılan bir post methodu var mı?
    if request.method=='POST':
        postcontent = request.POST['postcontent']
        if request.FILES.get('postimg'):
            postimg = request.FILES['postimg']
        grup=request.POST['grup']
        newPost = Post.objects.create(
            content = postcontent,
            image = postimg,
            yazar=request.user,
            grup_id=grup
        )
        newPost.save()
        return redirect('index')  

    context = {
        'postcontent':postcontent,
        'postimg':postimg,
        'topplulukadı':topplulukadı
    }      
   
    return render(request, 'post.html', context)

def kaydet(request):
    return render(request, 'saved.html')

def topluluk(request):
    topplulukadı=Toplulukolusturma.objects.all()

    context = {
       'topplulukadı':topplulukadı      
    }    
    return render(request, 'topluluklar.html',context)

@login_required(login_url='login')
def toplulukolusturma(request):
    toplulukadı = ''
    toplulukbg= ''
    toplulukpp=''
    #sayfada çalıştırılan bir post methodu var mı?
    if request.method=='POST':
        toplulukadı = request.POST['toplulukadı']
        if request.FILES.get('toplulukbg'):
            toplulukbg = request.FILES['toplulukbg']
        if request.FILES.get('toplulukpp'):
            toplulukpp = request.FILES['toplulukpp']
        
        newTopluluk = Toplulukolusturma.objects.create(
            toplulukadı = toplulukadı,
            toplulukbackgroundimg = toplulukbg,
            toplulukprofileimg=toplulukpp
        )

        newTopluluk.save()
        return redirect('topluluk')  

    context = {
        'toplulukadı':toplulukadı,
        'toplulukbg':toplulukbg,
        'toplulukpp':toplulukpp
    }     
    return render(request, 'toplulukolusturma.html',context)
