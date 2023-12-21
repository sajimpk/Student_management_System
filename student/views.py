from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import deparment,semister,sesson,CoustomUser
from .models import student

# Create your views here.
def add_student(request):
    user = request.user
    dpr = deparment.objects.all()
    semi = semister.objects.all()
    ses = sesson.objects.all()
    if request.method=='POST':
        fr_name = request.POST.get('frist_name')
        la_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        phone = request.POST.get('phone')
        roll = request.POST.get('roll')
        father_name = request.POST.get('father_name')
        father_num = request.POST.get('father_num')
        mother_name = request.POST.get('mother_name')
        Address = request.POST.get('Address')
        Deparment_id = request.POST.get('Deparment')
        sess_id = request.POST.get('sess')
        Semister_id = request.POST.get('Semister')
        if CoustomUser.objects.filter(email = email).exists():
            messages.success(request, " Email Already Taken.")
            return redirect('add_student')
        elif CoustomUser.objects.filter(username=username).exists():
            messages.success(request, " Username Already Taken.")
            return redirect('add_student')
        else:
            admin = CoustomUser(
                first_name = fr_name,
                last_name = la_name,
                username = username,
                email = email,
                profile_pic =image,
                user_type = "3",
                password = password,
            )
            admin.set_password(password)
            admin.save()
            sem = semister.objects.get ( id = Semister_id)
            ses = deparment.objects.get(id = Deparment_id)
            Dep = sesson.objects.get(id = sess_id)
            students = student.objects.create(
                admin = admin,
                phone = phone,
                roll = roll,
                father_name = father_name,
                father_num = father_num,
                mother_name = mother_name,
                Address = Address,
                Deparment = Dep,
                sess = ses,
                Semister = sem,
            )
            students.save()
            
            messages.success(request, "Student added")
            return redirect(request.META['HTTP_REFERER'])

    return render(request,'student/add.html',locals())