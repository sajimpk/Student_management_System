from django.urls import path
from .views import *
urlpatterns = [
    path('add-student/',add_student,name="add_student"),
    path('student_view/',student_view,name="student_view"),
    path('student_update/<int:id>/',student_update,name="student_update")

]
