from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

from company.models import Company
from .forms import RegisterUserForm
from .models import User
from resume.models import Resume

#Register application only
def register(request):
    return render(request,'users/register.html')

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request,'Congratulations ! you have created your account.')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong !')
            return redirect('register_applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register-applicant.html',context)

#Register Recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request,'Congratulations ! you have created your account.')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong !')
            return redirect('register_recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register-recruiter.html',context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email = email,password = password)
        print(email,password,user)
        if user != None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('login')
    else:
        return render(request,'users/login.html')
    
def logout_user(request):
    logout(request)
    messages.info(request,'Your sesson is end')
    return redirect('login')