from django.db import models
from account.models import CoustomUser,sesson,deparment,semister
# Create your models here.
class student(models.Model):
    admin = models.OneToOneField(CoustomUser,on_delete = models.CASCADE)
    phone = models.IntegerField()
    roll = models.IntegerField()
    father_name = models.CharField(max_length=35)
    father_num = models.IntegerField()
    mother_name = models.CharField(max_length=35)
    Address = models.TextField(max_length=60)
    Deparment = models.ForeignKey(deparment,on_delete=models.CASCADE)
    sess = models.ForeignKey(sesson,on_delete=models.CASCADE)
    Semister = models.ForeignKey(semister,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.admin.username +' || '+ self.admin.first_name + ' ' + self.admin.last_name