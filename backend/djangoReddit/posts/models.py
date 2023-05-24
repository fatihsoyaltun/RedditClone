from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Toplulukolusturma(models.Model):
    toplulukadı=models.CharField(max_length=100, null=True)
    toplulukbackgroundimg=models.FileField( upload_to='posts/' , null=True, blank=True )
    toplulukprofileimg=models.FileField( upload_to='posts/' , null=True, blank=True )

    def __str__(self):
        return self.toplulukadı
    

class Post(models.Model):
    yazar=models.ForeignKey(User,on_delete=models.CASCADE,null=True)    
    grup=models.ForeignKey(Toplulukolusturma,on_delete=models.CASCADE,null=True)   
    content = models.TextField(max_length=1000 )
    image=models.FileField( upload_to='posts/' , null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True,null=True, verbose_name='oluşturulma tarihi')
    # like = models.ManyToManyField(related_name='likes' , verbose_name='Begenenler' , blank=True)
    # dislike = models.ManyToManyField(related_name='dislikes' , verbose_name='Begenmeyenler' , blank=True)
    

    def __str__(self):
        return self.content
    
