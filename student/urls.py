from django.urls import path
from .views import *
urlpatterns = [
    path('add-student/',add_student,name="add_student")

]
