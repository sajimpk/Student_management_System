from django.db import models

# Create your models here.
class student(models.Model):
    phone = models.IntegerField()
    roll = models.IntegerField()
    father_name = models.CharField(max_length=35)
    father_num = models.IntegerField()
    mother_name = models.CharField(max_length=35)
    Address = models.TextField(max_length=60)
    Deparment = models.CharField(max_length=30)
    sess = models.CharField(max_length=20)
    Semister = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.father_name