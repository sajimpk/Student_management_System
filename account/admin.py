from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class usermodel(UserAdmin):
    list_display= ['username','user_type','first_name','last_name']
admin.site.register(CoustomUser,usermodel)
admin.site.register(sesson)
admin.site.register(semister)
admin.site.register(deparment)
