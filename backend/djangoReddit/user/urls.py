from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('profilayarlar/', profilayarlar, name='profilayarlar'),
    path('genelayarlar/', genelayarlar, name='genelayarlar'),
    path('login/', giris , name='login'),
    path('logout/', cikis , name='logout'),
    path('profil/' , profil , name='profil'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
