from django.db import models

# Create your models here.

class Post(models.Model):
    grup=models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100 , null=True)
    content = models.TextField(max_length=1000 )
    image=models.FileField( upload_to='posts/' , null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True,null=True, verbose_name='oluşturulma tarihi')

    def __str__(self):
        return self.title
    
