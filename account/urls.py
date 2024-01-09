from django.urls import path
from .views import *
urlpatterns = [
    path('login/',loginUser,name='login'),
    path('',home,name='home'),
    path('logout/',log_out,name='logout'),
    path('update_profile/',update_profile,name='update_profile'),
    path('password_update/',pass_update,name='pass_update'),
    path('profile/',profile,name='profile'),
    
    path('error/',error,name='error'),
    
]
