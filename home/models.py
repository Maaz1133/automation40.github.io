from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class home1(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    # phone = models.CharField(max_length=12)
    message1 = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class loginmyy(models.Model):
    name_login = models.CharField(max_length=122)
    email_login = models.CharField(max_length=122)
    # phone = models.CharField(max_length=12)
    message2 = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email_login   

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    img_url=models.URLField()
    content = models.TextField()
    content1 = RichTextField()
    URL= models.TextField(max_length=130)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
