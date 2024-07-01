from django.shortcuts import render,redirect,HttpResponse
from student.models import student
from .models import CoustomUser
import os
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def home (request):
    if request.user.is_authenticated:
        user = request.user
        if user.user_type=='1':
            return redirect('hod_dashbord')
        if user.user_type=='2':
            return redirect('staff_dashbord')
        if user.user_type=='3':
            return redirect('student_dashbord')
    else:
        return redirect('login')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            if user.user_type=='1':
                return redirect('hod_dashbord')
            if user.user_type=='2':
                return redirect('staff_dashbord')
            if user.user_type=='3':
                return redirect('student_dashbord')
        else:
            messages.warning(request, "Username and password incorrect .")
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')
def update_profile(request):
    user = request.user
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        a=user.username
        user_ = CoustomUser.objects.get(username=a)
        user_.username =username
        user_.email =email
        if image:
            if user.profile_pic == '1.jpeg':
                pass
            else:
                os.remove(user_.profile_pic.path)
                user_.profile_pic=image
        user_.save()
        messages.success(request, "Updated")
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'updateprofile.html',locals())

def pass_update(request):
    user = request.user
    if request.method=='POST':
        old_pass =request.POST.get('old_pass')
        passw =request.POST.get('pass')
        confrm_passw =request.POST.get('con_pass')
        if passw == confrm_passw:
            lenth = len(passw)
            if lenth < 5:
                messages.error(request, "password most be 6 charecter")
            else:
                check_ = user.check_password(old_pass)
                if check_:
                    a=user.id
                    user_ = CoustomUser.objects.get(id=a)
                    user_.password =passw
                    user_.set_password(passw)
                    user_.save()
                    messages.success(request, "password update success")
                    update_session_auth_hash(request, user_)
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    messages.warning(request, "Old Password incorrect")
        else:
            messages.warning(request, "confrom password not match")
    else:
        return redirect('error')
        

@login_required(login_url='login')
def profile(request):
    user = request.user
    try:
        if user.user_type == '3':
            detel = student.objects.get(admin=user)
        else:
            pass
    except Exception as e:
        return redirect('error')
    return render(request,'profile.html',locals())

@login_required(login_url='login')
def log_out(request):
    logout(request)
    messages.success(request,'log out success')
    return redirect('login')

def error(request):
    return render(request,"error.html")