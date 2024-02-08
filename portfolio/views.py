from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import User, Portfolio
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def index(request):
    return render(request, 'portfolio/index.html',{
        "user": request.user,
    })

@login_required(login_url="login_view")
def myporto(request):
    try:
        porto = Portfolio.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return render(request, 'portfolio/create.html')
    return render(request, 'portfolio/myporto.html',{
        'porto': porto,
        "portfolio" : porto
    })

@login_required(login_url="login_view")
def create(request):
    if request.method == 'GET':
        return render(request, 'portfolio/create.html')
    user = User.objects.get(username=request.user)
    name = request.POST['name']
    profession = request.POST['profession']
    description = request.POST['describe-yourself']
    phone = request.POST['phone']
    email = request.POST['email']
    project = request.POST['project']
    project_description = request.POST['project-description']
    link = request.POST['project-link']
    style = request.POST['styles']
    try:
        portfolio = Portfolio.objects.create(user=user,name=name,profession=profession, description=description, phone=phone, email=email, project=project,
                                         project_description=project_description, link=link, style=style)
        portfolio.save()
    except IntegrityError:
        return HttpResponse('already exists')
    print(style)
    return HttpResponse(style)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'portfolio/login.html',{
            "message": "Not valid username/password"
        })
    return render(request, 'portfolio/login.html')

def register(request):
    if request.method != 'POST':
        return render(request, 'portfolio/register.html')
    user = request.POST['username']
    password = request.POST['password']
    password_confirmation = request.POST['password-confirmation']
    print(user,password,password_confirmation)
    if not user or not password or not password_confirmation:
        return HttpResponse('that is not valid information')
    elif password != password_confirmation:
        return HttpResponse('password and password confirmation must be equal')
    user = User.objects.create_user(username=user, password=password)
    return HttpResponseRedirect(reverse('login_view'))

# Create your views here.
