from django.urls import path
from .views import *
urlpatterns = [
    path('staff-dashbord/',dashbord,name='staff_dashbord'),
    path('add-teacher/',add_staff,name="add_staff"),
    path('staff_view/',staff_view,name="staff_view"),
    path('staff_update/<int:id>/',staff_update,name="staff_update"),
    path('staff_delete/<int:id>/',staff_delete,name="staff_delete"),
]
