from django.db import models
from django.urls import reverse
# Create your models here.
class book(models.Model):
    
    
    title = models.CharField(max_length=100,null=True,blank=True)
    author= models.CharField(null=True,blank=True,max_length=100)
    isbn = models.BigIntegerField( )
    category= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.title) + " ["+str(self.isbn)+']'
   
