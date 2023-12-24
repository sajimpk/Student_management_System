from django.shortcuts import render,redirect,HttpResponse
from student.models import student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate, logout
# Create your views here.
@login_required(login_url='login')
def home (request):
    if request.user.is_authenticated:
        user = request.user
        return redirect('profile')
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
                return redirect('home')
            if user.user_type=='2':
                return HttpResponse('satff')
            if user.user_type=='3':
                return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')
def update_profile(request):
    user = request.user
    return render(request,'updateprofile.html',locals())

@login_required(login_url='login')
def profile(request):
    user = request.user
    try:
        detel = student.objects.get(admin=user)
    except:
        None
    return render(request,'profile.html',locals())

@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')