from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', index, name='index'),
    path('begeni/', begeni, name='begeni'),
    path('kaydet/', kaydet, name='kaydet'),
    path('detail/<int:postId>', detail, name='detail'),
    path('post/', post, name='post'),
    path('icerik/<int:toplulukId>/', icerik, name='icerik'),
    path('topluluk/' , topluluk , name='topluluk'),
    path('toplulukolusturma/', toplulukolusturma, name='toplulukolusturma'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)