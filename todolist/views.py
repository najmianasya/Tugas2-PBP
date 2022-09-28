from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.models import Task
from .forms import NewTaskForm

# Create your views here.
@login_required(login_url='/todolist/login/')

def show_todolist(request):
    username = request.user.username
    todo_list = Task.objects.filter(user=request.user)
    context = {
    'username': username,
    'todo_list': todo_list,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = Task()
            new_task.user = request.user
            new_task.date = datetime.datetime.now()
            new_task.title = form.cleaned_data['title']
            new_task.description = form.cleaned_data['description']
            new_task.is_finished = False

            new_task.save()
            return redirect('todolist:show_todolist')
    else:
        form = NewTaskForm()

    context = {'form': form}
    return render(request, 'create_task.html', context)

def update_task(request, id):
    task = Task.objects.get(pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')