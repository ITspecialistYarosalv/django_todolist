from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Task,Static
from django.contrib import messages
from .forms import CreateTaskForm,RegisterForm,LoginForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

@login_required
def main(request):
    tasks = Task.objects.filter(user = request.user)
    statistic = Static.objects.filter(user= request.user).first()
    return render(request,"base/task_list.html",{"tasks":tasks,"statistic":statistic})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("main")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect('register')
    else:
        return render(request, "base/login.html",{"form":form})
    return render(request,"base/login.html",{"form":form})

@csrf_protect
def register(request):
   form =RegisterForm()
   if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           email = form.cleaned_data['email']

           if User.objects.filter(email = email).exists():
              messages.info(request,"The user exists")
              return redirect("login")
           elif User.objects.filter(username = username).exists():
               messages.info(request, "The user exists")
               return redirect("login")
           else:
               user = User.objects.create(username=username,password = make_password(password),email = email)
               user.save()

               user = auth.authenticate(request, username=username, password=password)
               auth.login(request, user)

               return redirect('main')

   return render(request,"base/register.html",{"form":form})

@login_required
def task(request):
   return render(request,"base/task.html")

@login_required
def task_confirm(request,task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('main')
    return render(request, 'base/delete.html', {'task': task})


@login_required
def task_form(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            static, created = Static.objects.get_or_create(user=request.user)
            static.calculate_statistics()
            return redirect('main')
    return render(request, "base/task_form.html",{"form":form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def change_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.status == 'completed':
        task.status = 'incomplete'
    else:
        task.status = 'completed'
    task.save()
    return redirect('main')