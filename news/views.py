from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate ,login, logout
from .models import *


# Create your views here.

def is_operator(user):
    if user.groups.filter(name="Operator").exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    
    if request.user.groups.filter(name="Operator").exists():
        request.session['is_operator'] = 'operator'
    
    seeUse = User.objects.all()
    
    context = {
        "see" : seeUse
    }
    
    return render(request, template_name, context)

@login_required
def seeNews(request):
    
    template_name = "back/newsTable.html"
    
    allNews = News.objects.filter(penulis=request.user)
    
    context = {
        "data" : allNews
    }
    
    return render(request, template_name, context)

@login_required
def addNews(request):
    
    template_name = "back/newArtikel.html"
    
    if request.method == "POST":
        
        myfile = request.FILES.get("gambar")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        judul = request.POST.get('judul')
        konten = request.POST.get('konten')
        gambar = url
        penulis = request.user
        
        News.objects.create(
            penulis = penulis,
            judul = judul,
            konten = konten,
            picture = gambar
        )
        
        return redirect(seeNews)
    
    return render(request, template_name)

@login_required
def editNews(request, id):
    template_name = "back/newArtikel.html"
    
    get_artikel = News.objects.get(id=id)
    
    if request.method == "POST":
        
        myfile = request.FILES.get("gambar", False)
        
        judul = request.POST.get('judul')
        konten = request.POST.get('konten')
        penulis = request.user
        
        if(myfile):
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            gambar = url
            get_artikel.picture = gambar
        
        get_artikel.penulis = penulis
        get_artikel.judul = judul
        get_artikel.konten = konten
        get_artikel.save()
        
        
        return redirect(seeNews)
    
    context = {
        "value" : get_artikel
    }
    
    return render(request, template_name, context)

@login_required
def deleteNews(request, id):
    News.objects.get(id=id).delete()
    return redirect(seeNews)


@login_required
@user_passes_test(is_operator)
def register(request):
    
    template_name = "back/register.html"
    
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            
            User.objects.create(
                username = username,
                password = make_password(get_password),
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            
            return redirect(dashboard)
    
    return render(request, template_name)

@login_required
@user_passes_test(is_operator)
def editUser(request, id):
    template_name= "back/register.html"
    
    get_user = User.objects.get(id=id)
    
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            
            get_user.username = username
            get_user.password = make_password(get_password)
            get_user.first_name = first_name
            get_user.last_name = last_name
            get_user.email = email
            get_user.save()
            
            return redirect(dashboard)
        
    context = {
        "users" : get_user
    }
            
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def hapusUsers(request, id):
    User.objects.get(id=id).delete()
    return redirect(dashboard)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('home')