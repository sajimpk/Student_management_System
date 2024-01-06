from django.db import models
from account.models import CoustomUser,sesson,deparment,semister
# Create your models here.
class staff(models.Model):
    gen = (
        ('male','male'),
        ('female','female'),
        ('other','other'),
    )
    admin = models.OneToOneField(CoustomUser,on_delete = models.CASCADE)
    phone = models.IntegerField()
    Address = models.TextField(max_length=60)
    gender  = models.CharField(choices = gen,max_length=8)
    def __str__(self) -> str:
        return self.admin.username +' || '+ self.admin.first_name + ' ' + self.admin.last_name