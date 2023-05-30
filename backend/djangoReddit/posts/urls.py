from django.urls import path
from .views import *



urlpatterns =[
    path('', index, name='index'),
    path('begeni/', begeni, name='begeni'),
    path('kaydet/', kaydet, name='kaydet'),
    path('detail/<int:postId>', detail, name='detail'),
    path('post/', post, name='post'),
    path('icerik/<int:toplulukId>/', icerik, name='icerik'),
    path('topluluk/' , topluluk , name='topluluk'),
    path('toplulukolusturma/', toplulukolusturma, name='toplulukolusturma'),

]