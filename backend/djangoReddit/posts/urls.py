from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', index, name='index'),
    path('begeni/', begeni, name='begeni'),
    path('detail/<int:id>', detail, name='detail'),
    path('post/', post, name='post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)