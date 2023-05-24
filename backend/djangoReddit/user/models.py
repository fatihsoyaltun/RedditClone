from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , verbose_name='isim')
    surname = models.CharField(max_length=100 , verbose_name='Soyisim')
    bio = models.TextField(max_length=500 , verbose_name='Hakkinda' , default='Merhaba')
    image = models.FileField(upload_to='profiles/' , null=True , verbose_name='Profil Resmi' , default='profiles/default.jpg')
    backimage = models.FileField(upload_to='profiles/' , null=True , verbose_name='Profil')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='Olusturulma Tarihi')

    def __str__(self):
        return self.user.username
