from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    yazar=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    grup=models.CharField(max_length=100, null=True)
    userName = models.CharField(max_length=100 , null=True)
    content = models.TextField(max_length=1000 )
    image=models.FileField( upload_to='posts/' , null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True,null=True, verbose_name='oluşturulma tarihi')

    def __str__(self):
        return self.yazar.username
    
