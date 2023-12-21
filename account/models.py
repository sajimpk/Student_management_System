from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CoustomUser(AbstractUser):
    USER = (
        ('1','hod'),
        ('2','staff'),
        ('3','student'),
    )
    user_type =models.CharField(choices=USER,max_length=20)
    profile_pic = models.ImageField(upload_to='profile_pic/',default='1.jpeg')
    

class deparment(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
class semister(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
class sesson(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name