from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import CoustomUser
from .models import *
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
@login_required(login_url='login')
def dashbord(request):
    if request.user.user_type=='2':
        pass
    else:
        return redirect('error')
    return render(request,'staff/home.html')

@login_required(login_url='login')
def add_staff(request):
    if request.user.user_type=='1':
        if request.method=='POST':
            fr_name = request.POST.get('frist_name')
            la_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            image = request.FILES.get('image')

            phone = request.POST.get('phone')
            Address = request.POST.get('Address')
            gender = request.POST.get('gender')
            if CoustomUser.objects.filter(email = email).exists():
                messages.warning(request, " Email Already Taken.")
                return redirect('add_staff')
            elif CoustomUser.objects.filter(username=username).exists():
                messages.warning(request, " Username Already Taken.")
                return redirect('add_staff')
            else:
                admin = CoustomUser(
                    first_name = fr_name,
                    last_name = la_name,
                    username = username,
                    email = email,
                    user_type = "2",
                    password = password,
                )
                if image:
                    admin.profile_pic=image
                admin.set_password(password)
                admin.save()
                students = staff.objects.create(
                    admin = admin,
                    phone = phone,
                    Address = Address,
                    gender = gender,
                )
                students.save()
                
                messages.success(request, "Staff added")
                return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('error')
    return render(request,'staff/add_staff.html')

@login_required(login_url='login')
def staff_view(request):
    if request.user.user_type=='1':
        detel = staff.objects.all()
    else:
        return redirect('error')
    return render(request,'staff/view_staff.html',locals())

@login_required(login_url='login')
def staff_update(request,id):
    if request.user.user_type=='1':
        detel = staff.objects.get(id=id)
        try:
            
            if request.method=='POST':
                fr_name = request.POST.get('frist_name')
                la_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                passw = request.POST.get('password')
                image = request.FILES.get('image')
                phone = request.POST.get('phone')
                Address = request.POST.get('Address')
                gender = request.POST.get('gender')
                
                

                if detel:
                    detel.admin.first_name = fr_name
                    detel.admin.last_name = la_name
                    detel.admin.email = email
                    detel.admin.username =username
                    detel.phone = phone
                    detel.Address=Address
                    if passw:
                        detel.admin.password = passw
                        detel.admin.set_password(passw)
                        messages.warning(request, "Password Changed")
                    if image:
                        os.remove(detel.admin.profile_pic.path)
                        detel.admin.profile_pic = image
                    if gender:
                        detel.gender = gender
                    detel.admin.save()
                    detel.save()
                    messages.success(request, "Update Success")
                
        except Exception as r:
            return redirect('error')
    else:
        return redirect('error')
    return render(request,'staff/staff_update.html',locals())

@login_required(login_url='login')
def staff_delete(request,id):
    if request.user.user_type=='1':
        user = staff.objects.get(id = id)
        if user.admin.profile_pic:
            if user.admin.profile_pic == '1.jpeg':
                pass
            else:
                os.remove(user.admin.profile_pic.path)
        user.admin.delete()
        user.delete()
        messages.success(request, "Staff delete success")
    else:
        return redirect('error')
    return redirect('staff_view')