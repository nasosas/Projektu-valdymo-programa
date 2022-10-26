from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Project, Client, Employee
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


def index(request):

    num_projects = Project.objects.all().count()
    num_employees = Employee.objects.all().count()
    num_clients = Client.objects.all().count()
    context = {
        'num_projects': num_projects,
        'num_employees': num_employees,
        'num_clients': num_clients,
    }
    return render(request, 'index.html', context=context)


def projects(request):
    paginator = Paginator(Project.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_projects = paginator.get_page(page_number)
    context = {
        'projects': paged_projects
    }
    return render(request, 'projects.html', context=context)


def project(request, project_id):
    single_project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project.html', {'project': single_project})


def employee(request):
    employe = Employee.objects.all()
    context = {
        'employe': employe
    }
    print(employe)
    return render(request, 'employee.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Project.objects.filter(Q(name__icontains=query))
    context = {
        'projects': search_results,
        'query': query,
    }
    return render(request, 'search.html', context=context)


def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'clients.html', context=context)


def client(request, client_id):
    single_client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client.html', {'client': single_client})

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with this email {email} is already in use')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'registration/register.html')