from django.shortcuts import render,redirect
from account.models import deparment,semister,sesson
from student.models import student
from staff.models import staff,Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashbord(request):
    if request.user.user_type=='1':
        student_count = student.objects.all().count()
        staff_count = staff.objects.all().count()
        deparment_count = deparment.objects.all().count()
        sub_count = Subject.objects.all().count()
    else:
        return redirect('error')
    return render(request,'hod/dashbord.html',locals())

@login_required(login_url='login')
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
            return redirect('error')
    return render(request,'hod/for_add/deperment_add.html')

@login_required(login_url='login')
def viw_deperment(request):
    if request.user.user_type=='1':
        deper = deparment.objects.all()
    else:
        return redirect('error')
    
    return render(request,'hod/for_add/view_deperment.html',locals())

@login_required(login_url='login')
def deperment_delete(request,id):
    if request.user.user_type=='1':
        depermenT = deparment.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "Deperment Deleted")
        return redirect('viw_deperment')
    else:
        return redirect('error')



# -------------------------------------------
@login_required(login_url='login')
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
            return redirect('error')
    return render(request,'hod/for_add/semister_add.html')

@login_required(login_url='login')
def viw_semister(request):
    if request.user.user_type=='1':
        deper = semister.objects.all()
    else:
        messages.error(request, "error 404")
        return redirect('home')
    return render(request,'hod/for_add/view_semister.html',locals())

@login_required(login_url='login')
def semister_delete(request,id):
    if request.user.user_type=='1':
        depermenT = semister.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "semister Deleted")
        return redirect('viw_semister')
    else:
        return redirect('error')
# -------------------------------------------
@login_required(login_url='login')
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
        return redirect('error')
    return render(request,'hod/for_add/sesson_add.html')

@login_required(login_url='login')
def viw_sesson(request):
    if request.user.user_type=='1':
        deper = sesson.objects.all()
    else:
        return redirect('error')
    return render(request,'hod/for_add/view_sesson.html',locals())

@login_required(login_url='login')
def sesson_delete(request,id):
    if request.user.user_type=='1':
        depermenT = sesson.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "sesson Deleted")
        return redirect('viw_sesson')
    else:
        return redirect('error')
# -------------------------------------------

@login_required(login_url='login')
def add_subject(request):
    if request.user.user_type=='1':
        semis = semister.objects.all()
        teacher = staff.objects.all()
        if request.method=='POST':
            name = request.POST.get('name')
            smister = request.POST.get('smister')
            staf = request.POST.get('staff')
            _semister = semister.objects.get ( id = smister)
            _staff = staff.objects.get ( id = staf)
            if Subject.objects.filter(name = name).exists():
                messages.warning(request, "subject Alredy exist")
            else:
                add = Subject.objects.create(
                    name = name,
                    Semister = _semister,
                    staff = _staff,
                )
                add.save()
                messages.success(request, "Sesson Added")

    else:
        return redirect('error')
    return render(request,'hod/for_add/subject_add.html',locals())
        
@login_required(login_url='login')
def edit_subject(request,id):
    
        if request.user.user_type=='1':
            semis = semister.objects.all()
            teacher = staff.objects.all()
            sub = Subject.objects.get(id=id)
            if request.method=='POST':
                    name = request.POST.get('name')
                    smister = request.POST.get('smister')
                    staf = request.POST.get('staff')
                    if sub:
                        sub.name = name
                        if staf:
                            _staff = staff.objects.get( id = staf)
                            sub.staff = _staff
                        if smister:
                            _semister = semister.objects.get( id = smister)
                            sub.Semister=_semister
                        messages.success(request, "Update Success")
                        sub.save()

        else:
            messages.error(request, "error 404")
            return redirect('home')
        return render(request,'hod/for_add/edit_sub.html',locals())
        
@login_required(login_url='login')
def viw_subject(request):
    if request.user.user_type=='1':
        deper = Subject.objects.all()
    else:
        return redirect('error')
    return render(request,'hod/for_add/view_subject.html',locals())

@login_required(login_url='login')
def subject_delete(request,id):
    if request.user.user_type=='1':
        depermenT = Subject.objects.get(id=id)
        depermenT.delete()
        messages.success(request, "sesson Deleted")
        return redirect('viw_subject')
    else:
        return redirect('error')
    