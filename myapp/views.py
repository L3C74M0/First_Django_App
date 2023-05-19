from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateTask, CreateProject

def index(request):
  title = 'Django Home'
  return render(request, "index.html", {
    'title': title
  })


def hello(request, username):
  return HttpResponse("Hello %s" % username)


def about(request):
  username = 'User'
  return render(request, "about.html", {
    'user': username
  })


def projects(request):
  #projects = list(Project.objects.values())
  projects = Project.objects.all()
  return render(request, 'projects/projects.html', {
    'projects': projects
  })


def tasks(request):
  #task = get_object_or_404(Task)
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks
  })

def create_task(request):
  if request.method == 'GET':
    return render(request, 'tasks/create_task.html', {
      'form': CreateTask()
    })
  else:
    Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
    return redirect('tasks')


def create_project(request):
  if request.method == 'GET':
    return render(request, 'projects/create_project.html', {
      'form': CreateProject()
    })
  else:
    Project.objects.create(name=request.POST['name'])
    return redirect('projects')
  
def project_detail(request, id):
  project = get_object_or_404(Project,id=id)
  tasks = Task.objects.filter(project_id=id)
  print(tasks)
  return render(request, 'projects/detail.html', {
    'project': project,
    'tasks': tasks
  })