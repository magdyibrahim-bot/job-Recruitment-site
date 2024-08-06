from django.shortcuts import render
from tkinter.messagebox import showerror
from django.shortcuts import redirect
from atexit import register
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import UserForm
from .models import AdminForm
from .models import JobForm
from .forms import LoginForm
from .forms import UserSignUp
from .forms import AdminSignUp
from .forms import Form
from django.http import HttpResponse

def signupuser(request):
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            mail = form.cleaned_data['mail']
            talent = form.cleaned_data['talent']
            rePassword = form.cleaned_data['rePassword']
            user = UserForm.objects.filter(name=username).first()
            if password == rePassword:
                if user:
                    form.add_error(None, "There is a User with data info.")
                else:
                    data = UserForm(name = username,
                                    mail = mail,
                                    password = password,
                                    talanet = talent)
                    data.save()
                    return redirect('login')
            else:
                form.add_error(None, "The password don't Match.")
    else:
        form = UserSignUp()
    return render(request,'pages/usersignup.html',{'form':form})
    

def signupadmin(request):
    if request.method == 'POST':
        form = AdminSignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            mail = form.cleaned_data['mail']
            companyName = form.cleaned_data['companyName']
            rePassword = form.cleaned_data['rePassword']
            admin = AdminForm.objects.filter(name=username).first()
            if password == rePassword:
                if admin:
                    form.add_error(None, "There is a Admin with data info.")
                else:
                    data = AdminForm(name = username,
                                    mail = mail,
                                    password = password,
                                    companyName = companyName)
                    data.save()
                    return redirect('login')
            else:
                form.add_error(None, "The password don't Match.")
    else:
        form = AdminSignUp()
    return render(request,'pages/adminsignup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            option = form.cleaned_data['option']
            if option == 'option2':
                admin = AdminForm.objects.filter(name=username, password=password).first()
                if admin:
                    return redirect('admin')
                else:
                    form.add_error(None, "Invalid username or password.")
            else:
                user = UserForm.objects.filter(name=username, password=password).first()
                if user:
                    return redirect('user')
                else:
                    form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request,'pages/login.html',{'form': form})

def admin(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            salary = form.cleaned_data['salary']
            tilte = form.cleaned_data['title']
            companyName = form.cleaned_data['companyName']
            status = form.cleaned_data['status']
            description = form.cleaned_data['description']
            job = JobForm(number = number,
                          salary = salary,
                          title = tilte,
                          companyName = companyName,
                          status = status,
                          description = description)
            job.save()
    else:
        form = Form()
    return render(request,'pages/adminPagefm.html',{'form':form})

def available(request):
    return render(request,'pages/adminpage_tb.html',{'job': JobForm.objects.all()})

def user(request):
    return render(request, 'pages/userPage.html', {'job': JobForm.objects.filter(status = 'Opened')})

def index(request):
    return render(request,'pages/index.html')

def contact(request):
    return render(request,'pages/contact.html')

def apply(request):
    return render(request,'pages/Apply.html')