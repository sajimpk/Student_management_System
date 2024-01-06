from django.shortcuts import render,redirect
from account.models import deparment,semister,sesson
from student.models import student
from staff.models import staff
from django.contrib import messages

# Create your views here.
def dashbord(request):
    if request.user.user_type=='1':
        pass
    else:
        messages.error(request,'somthin error')
        return redirect('home')
    return render(request,'hod/dashbord.html')

def add_deperment(request):
    if request.user.user_type=='1':
        if request.method=='POST':
            name = request.POST.get('name')
            if deparment.objects.filter(name = name).exists():
                messages.warning(request, "Deperment Alredy exist")
            else:
                add = deparment.objects.create(
                    name = name
                )
                add.save()
                messages.success(request, "Deperment Added")
        else:
            messages.error(request, "error 404")
            return redirect('home')
    return render(request,'hod/for_add/deperment_add.html')

def viw_deperment(request):
    if request.user.user_type=='1':
        deper = deparment.objects.all()
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/view_deperment.html',locals())

def deperment_delete(request,id):
    if request.user.user_type=='1':
        depermenT = deparment.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "Deperment Deleted")
        return redirect('viw_deperment')
    else:
        messages.error(request, "error 404")
        return redirect('home')



# -------------------------------------------
def add_semister(request):
    if request.user.user_type=='1':
        if request.method=='POST':
            name = request.POST.get('name')
            if semister.objects.filter(name = name).exists():
                messages.warning(request, "Semister Alredy exist")
            else:
                add = semister.objects.create(
                    name = name
                )
                add.save()
                messages.success(request, "Semister Added")
        else:
            messages.error(request, "error 404")
            return redirect('home')
    return render(request,'hod/for_add/semister_add.html')

def viw_semister(request):
    if request.user.user_type=='1':
        deper = semister.objects.all()
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/view_semister.html',locals())

def semister_delete(request,id):
    if request.user.user_type=='1':
        depermenT = semister.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "semister Deleted")
        return redirect('viw_semister')
    else:
        messages.error(request, "error 404")
        return redirect('home')
# -------------------------------------------
def add_sesson(request):
    if request.user.user_type=='1':
        if request.method=='POST':
            name = request.POST.get('name')
            if sesson.objects.filter(name = name).exists():
                messages.warning(request, "Sesson Alredy exist")
            else:
                add = sesson.objects.create(
                    name = name
                )
                add.save()
                messages.success(request, "Sesson Added")
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/sesson_add.html')

def viw_sesson(request):
    if request.user.user_type=='1':
        deper = sesson.objects.all()
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/view_sesson.html',locals())

def sesson_delete(request,id):
    if request.user.user_type=='1':
        depermenT = sesson.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "sesson Deleted")
        return redirect('viw_sesson')
    else:
        messages.error(request, "error 404")
        return redirect('home')
# -------------------------------------------
def add_subject(request):
    if request.user.user_type=='1':
        semis = semister.objects.all()
        teacher = staff.objects.all()

    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/subject_add.html',locals())
        

def viw_subject(request):
    if request.user.user_type=='1':
        deper = None
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/view_subject.html',locals())

def subject_delete(request,id):
    if request.user.user_type=='1':
        messages.success(request, "sesson Deleted")
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return redirect('viw_subject')