from django.shortcuts import render
from account.models import deparment,semister,sesson

# Create your views here.
def add_student(request):
    dpr = deparment.objects.all()
    semi = semister.objects.all()
    ses = sesson.objects.all()
    if request.method=="POST":
        frist_name = request.POST.get['frist_name']
        last_name = request.POST.get['last_name']
        email = request.POST.get['email']
        username = request.POST.get['username']
        password = request.POST.get['password']
        image = request.file.get['image']
        phone = request.POST.get['phone']
        roll = request.POST.get['roll']
        father_name = request.POST.get['father_name']
        father_num = request.POST.get['father_num']
        mother_name = request.POST.get['mother_name']
        Address = request.POST.get['Address']
        Deparment = request.POST.get['Deparment']
        sess  = request.POST.get['sess']
        Semister = request.POST.get['Semister']
        
    return render(request,'student/add.html',locals())