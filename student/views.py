from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import deparment,semister,sesson,CoustomUser
from .models import student
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
@login_required(login_url='login')
def dashbord(request):
    if request.user.user_type=='3':
        pass
    else:
        return redirect('error')
    return render(request,'student/dashbord.html')

@login_required(login_url='login')
def add_student(request):
    if request.user.user_type=='1':
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
                messages.warning(request, " Email Already Taken.")
                return redirect('add_student')
            elif CoustomUser.objects.filter(username=username).exists():
                messages.warning(request, " Username Already Taken.")
                return redirect('add_student')
            else:
                admin = CoustomUser(
                    first_name = fr_name,
                    last_name = la_name,
                    username = username,
                    email = email,
                    user_type = "3",
                    password = password,
                )
                if image:
                    admin.profile_pic=image
                admin.set_password(password)
                admin.save()

                sem = semister.objects.get ( id = Semister_id)
                Dep = deparment.objects.get(id = Deparment_id)
                sese= sesson.objects.get(id = sess_id)

                students = student.objects.create(
                    admin = admin,
                    phone = phone,
                    roll = roll,
                    father_name = father_name,
                    father_num = father_num,
                    mother_name = mother_name,
                    Address = Address,
                    Deparment = Dep,
                    sess = sese,
                    Semister = sem,
                )
                students.save()
                
                messages.success(request, "Student added")
                return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('error')
    return render(request,'student/add.html',locals())

@login_required(login_url='login')
def student_view(request):
    if request.user.user_type=='1':
        detel = student.objects.all()
    else:
        return redirect('error')
    return render(request,'student/students.html',locals())
    
@login_required(login_url='login')
def student_update(request,id):
    if request.user.user_type=='1':
        dpr = deparment.objects.all()
        semi = semister.objects.all()
        ses = sesson.objects.all()
        detel = student.objects.get(id=id)
        try:
            
            if request.method=='POST':
                fr_name = request.POST.get('frist_name')
                la_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                passw = request.POST.get('password')
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
                
                
                

                if detel:
                    detel.phone = phone
                    detel.roll = roll
                    detel.father_name = father_name
                    detel.father_num = father_num
                    detel.mother_name = mother_name
                    detel.Address=Address
                    detel.admin.first_name = fr_name
                    detel.admin.last_name = la_name
                    detel.admin.email = email
                    detel.admin.username =username
                    if passw:
                        detel.admin.password = passw
                        detel.admin.set_password(passw)
                        messages.success(request, "Password update")
                    if image:
                        os.remove(detel.admin.profile_pic.path)
                        detel.admin.profile_pic = image
                    if Deparment_id:
                        Dep = deparment.objects.get(id = Deparment_id)
                        detel.Deparment = Dep
                    if sess_id:
                        sesen= sesson.objects.get(id = sess_id)
                        detel.sess = sesen
                    if Semister_id:
                        sem = semister.objects.get ( id = Semister_id)
                        detel.Semister = sem
                    detel.admin.save()
                    detel.save()
                    messages.success(request, "Student update")
                
        except Exception as r:
            messages.warning(request, r)
    else:
        return redirect('error')
    return render(request,'student/update.html',locals())

@login_required(login_url='login')
def student_delete(request,id):
    if request.user.user_type=='1':
        user = student.objects.get(id = id)
        if user.admin.profile_pic:
            if user.admin.profile_pic == '1.jpeg':
                pass
            else:
                os.remove(user.admin.profile_pic.path)
        user.admin.delete()
        user.delete()
        messages.success(request, "Student delete success")
    else:
        return redirect('error')
    return redirect('student_view')


