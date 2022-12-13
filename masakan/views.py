from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from news.models import *
import requests

def homePage(request):
    template_name = "front/homePage.html"
    
    URL = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    URL2 = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r2 = requests.get(url = URL2)
    
    data2 = r2.json()
    
    URL3 = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r3 = requests.get(url = URL3)
    
    data3 = r3.json()
    
    URL4 = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r4 = requests.get(url = URL4)
    
    data4 = r4.json()
    
    URL5 = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r5 = requests.get(url = URL5)
    
    data5= r5.json()
    
    art = News.objects.all()
    
    p = Paginator(News.objects.all(), 3)
    page = request.GET.get('page')
    pager =p.get_page(page)
    nums = "a" * pager.paginator.num_pages
    
    context ={
       
        "data1" : data['meals'][0],
        "data2" : data2['meals'][0],
        "data3" : data3['meals'][0],
        "data4" : data4['meals'][0],
        "data5" : data5['meals'][0],
        "art" : art,
        "pager" : pager,
        "nums" : nums
    }
    
    return render(request, template_name, context)

def aboutMe(request):
    
    template_name = "front/aboutme.html"
    
    return render(request, template_name)

def blog(request):
    
    template_name = "front/blog.html"
    
    art = News.objects.all()
    
    p = Paginator(News.objects.all(), 3)
    page = request.GET.get('page')
    pager =p.get_page(page)
    nums = "a" * pager.paginator.num_pages
    
    context ={
       
        
        "art" : art,
        "pager" : pager,
        "nums" : nums
    }
    
    return render(request, template_name, context)

def detailBlog(request, id):
     template_name = "front/detailBlog.html"
     
     detail = News.objects.get(id=id)
     
     context = {
         "detail" : detail
     }
     
     return render(request, template_name, context)

def search(request):
    
    template_name = "front/search.html"
    
    global search
    
    search = request.POST.get('search')
    
    URL = "http://www.themealdb.com/api/json/v1/1/search.php?s={}".format(search)
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context = {
        "data" : data['meals']
    }
    
    return render(request, template_name, context)

def detailresep(request, id):
    
    template_name = "front/detailresep.html"
    
    URL = "http://www.themealdb.com/api/json/v1/1/lookup.php?i={}".format(id)
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    space = range(20)
    
    context = {
        "data" : data['meals'][0],
        "range" : space
    }
    
    return render(request, template_name, context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    template_name = "front/login.html"
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("login gagal")
    
    return render(request, template_name)