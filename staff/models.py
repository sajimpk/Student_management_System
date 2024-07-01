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
class Subject(models.Model):
    name = models.CharField(max_length = 20)
    Semister = models.ForeignKey(semister,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name +' || '+ self.Semister.name + ' || ' + self.staff.admin.first_name