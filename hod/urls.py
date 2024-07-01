from django.urls import path
from .views import *
urlpatterns = [
    path('dashbord/',dashbord,name='hod_dashbord'),
    path('deperment-add/',add_deperment,name='add_deperment'),
    path('deperment-list/',viw_deperment,name='viw_deperment'),
    path('semister-add/',add_semister,name='add_semister'),
    path('semister-list/',viw_semister,name='viw_semister'),
    path('sesson-add/',add_sesson,name='add_sesson'),
    path('sesson-list/',viw_sesson,name='viw_sesson'),
    path('subject-add/',add_subject,name='add_subject'),
    path('subject-list/',viw_subject,name='viw_subject'),

    path('semister_delete/<int:id>/',semister_delete,name="semister_delete"),
    path('deperment_delete/<int:id>/',deperment_delete,name="deperment_delete"),
    path('sesson_delete/<int:id>/',sesson_delete,name="sesson_delete"),
    path('subject_delete/<int:id>/',subject_delete,name="subject_delete"),
    path('subject-edit/<int:id>/',edit_subject,name="subject_edit"),

]
