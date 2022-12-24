from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from news.models import *
import requests
import random
from django.db.models import Q


def sinkron_masakan_random(request):
    URL = "http://www.themealdb.com/api/json/v1/1/random.php?"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    for d in data['meals']:
        cek_masakan = Masakan.objects.filter(idMeal=d['idMeal'])
        if cek_masakan.exists():
            resep = cek_masakan.first()   
            resep.idMeal = d['idMeal']         
            resep.strArea = d['strArea'] 
            resep.strCategory = d['strCategory'] 
            resep.strMeal = d['strMeal']
            resep.strMealThumb = d['strMealThumb']
            resep.strInstructions = d['strInstructions']
            resep.strYoutube = d['strYoutube']
            resep.strIngredient1 = d['strIngredient1']
            resep.strIngredient2 = d['strIngredient2'] 
            resep.strIngredient3 = d['strIngredient3'] 
            resep.strIngredient4 = d['strIngredient4'] 
            resep.strIngredient5 = d['strIngredient5'] 
            resep.strIngredient6 = d['strIngredient6'] 
            resep.strIngredient7 = d['strIngredient7'] 
            resep.strIngredient8 = d['strIngredient8'] 
            resep.strIngredient9 = d['strIngredient9'] 
            resep.strIngredient10 = d['strIngredient10'] 
            resep.strIngredient11 = d['strIngredient11'] 
            resep.strIngredient12 = d['strIngredient12'] 
            resep.strIngredient13 = d['strIngredient13'] 
            resep.strIngredient14 = d['strIngredient14'] 
            resep.strIngredient15 = d['strIngredient15'] 
            resep.strIngredient16 = d['strIngredient16'] 
            resep.strIngredient17 = d['strIngredient17'] 
            resep.strIngredient18 = d['strIngredient18'] 
            resep.strIngredient19 = d['strIngredient19'] 
            resep.strIngredient20 = d['strIngredient20'] 
            resep.strMeasure1 = d['strMeasure1'] 
            resep.strMeasure2 = d['strMeasure2'] 
            resep.strMeasure3 = d['strMeasure3'] 
            resep.strMeasure4 = d['strMeasure4'] 
            resep.strMeasure5 = d['strMeasure5'] 
            resep.strMeasure6 = d['strMeasure6'] 
            resep.strMeasure7 = d['strMeasure7'] 
            resep.strMeasure8 = d['strMeasure8'] 
            resep.strMeasure9 = d['strMeasure9'] 
            resep.strMeasure10 = d['strMeasure10'] 
            resep.strMeasure11 = d['strMeasure11'] 
            resep.strMeasure12 = d['strMeasure12'] 
            resep.strMeasure13 = d['strMeasure13'] 
            resep.strMeasure14 = d['strMeasure14'] 
            resep.strMeasure15 = d['strMeasure15'] 
            resep.strMeasure16 = d['strMeasure16'] 
            resep.strMeasure17 = d['strMeasure17'] 
            resep.strMeasure18 = d['strMeasure18'] 
            resep.strMeasure19 = d['strMeasure19'] 
            resep.strMeasure20 = d['strMeasure20'] 
            resep.save()
        else:
            Masakan.objects.create(
                idMeal = d['idMeal'],         
                strArea = d['strArea'], 
                strCategory = d['strCategory'], 
                strMeal = d['strMeal'],
                strMealThumb = d['strMealThumb'],
                strInstructions = d['strInstructions'],
                strYoutube = d['strYoutube'],
                strIngredient1 = d['strIngredient1'],
                strIngredient2 = d['strIngredient2'], 
                strIngredient3 = d['strIngredient3'], 
                strIngredient4 = d['strIngredient4'],
                strIngredient5 = d['strIngredient5'], 
                strIngredient6 = d['strIngredient6'], 
                strIngredient7 = d['strIngredient7'], 
                strIngredient8 = d['strIngredient8'], 
                strIngredient9 = d['strIngredient9'], 
                strIngredient10 = d['strIngredient10'], 
                strIngredient11 = d['strIngredient11'], 
                strIngredient12 = d['strIngredient12'], 
                strIngredient13 = d['strIngredient13'], 
                strIngredient14 = d['strIngredient14'], 
                strIngredient15 = d['strIngredient15'], 
                strIngredient16 = d['strIngredient16'], 
                strIngredient17 = d['strIngredient17'], 
                strIngredient18 = d['strIngredient18'], 
                strIngredient19 = d['strIngredient19'], 
                strIngredient20 = d['strIngredient20'], 
                strMeasure1 = d['strMeasure1'], 
                strMeasure2 = d['strMeasure2'], 
                strMeasure3 = d['strMeasure3'], 
                strMeasure4 = d['strMeasure4'], 
                strMeasure5 = d['strMeasure5'], 
                strMeasure6 = d['strMeasure6'], 
                strMeasure7 = d['strMeasure7'], 
                strMeasure8 = d['strMeasure8'], 
                strMeasure9 = d['strMeasure9'], 
                strMeasure10 = d['strMeasure10'], 
                strMeasure11 = d['strMeasure11'], 
                strMeasure12 = d['strMeasure12'], 
                strMeasure13 = d['strMeasure13'],
                strMeasure14 = d['strMeasure14'], 
                strMeasure15 = d['strMeasure15'], 
                strMeasure16 = d['strMeasure16'], 
                strMeasure17 = d['strMeasure17'], 
                strMeasure18 = d['strMeasure18'], 
                strMeasure19 = d['strMeasure19'], 
                strMeasure20 = d['strMeasure20'],
                
            )
    return HttpResponse("<h1>Berhasil connect API</h1>")

def homePage(request):
    template_name = "front/homePage.html"
    
    data = Masakan.objects.all()
    
    art = News.objects.all()
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    
    p = Paginator(News.objects.all(), 3)
    page = request.GET.get('page')
    pager =p.get_page(page)
    nums = "a" * pager.paginator.num_pages
    
    context ={
       
        "data1" : data[random.choice(list1)],
        "data2" : data[random.choice(list1)],
        "data3" : data[random.choice(list1)],
        "data4" : data[random.choice(list1)],
        "data5" : data[random.choice(list1)],
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
    
    try:
        for d in data['meals']:
            cek_masakan = Masakan.objects.filter(idMeal=d['idMeal'])
            if cek_masakan.exists():
                resep = cek_masakan.first()   
                resep.idMeal = d['idMeal']         
                resep.strArea = d['strArea'] 
                resep.strCategory = d['strCategory'] 
                resep.strMeal = d['strMeal']
                resep.strMealThumb = d['strMealThumb']
                resep.strInstructions = d['strInstructions']
                resep.strYoutube = d['strYoutube']
                resep.strIngredient1 = d['strIngredient1']
                resep.strIngredient2 = d['strIngredient2'] 
                resep.strIngredient3 = d['strIngredient3'] 
                resep.strIngredient4 = d['strIngredient4'] 
                resep.strIngredient5 = d['strIngredient5'] 
                resep.strIngredient6 = d['strIngredient6'] 
                resep.strIngredient7 = d['strIngredient7'] 
                resep.strIngredient8 = d['strIngredient8'] 
                resep.strIngredient9 = d['strIngredient9'] 
                resep.strIngredient10 = d['strIngredient10'] 
                resep.strIngredient11 = d['strIngredient11'] 
                resep.strIngredient12 = d['strIngredient12'] 
                resep.strIngredient13 = d['strIngredient13'] 
                resep.strIngredient14 = d['strIngredient14'] 
                resep.strIngredient15 = d['strIngredient15'] 
                resep.strIngredient16 = d['strIngredient16'] 
                resep.strIngredient17 = d['strIngredient17'] 
                resep.strIngredient18 = d['strIngredient18'] 
                resep.strIngredient19 = d['strIngredient19'] 
                resep.strIngredient20 = d['strIngredient20'] 
                resep.strMeasure1 = d['strMeasure1'] 
                resep.strMeasure2 = d['strMeasure2'] 
                resep.strMeasure3 = d['strMeasure3'] 
                resep.strMeasure4 = d['strMeasure4'] 
                resep.strMeasure5 = d['strMeasure5'] 
                resep.strMeasure6 = d['strMeasure6'] 
                resep.strMeasure7 = d['strMeasure7'] 
                resep.strMeasure8 = d['strMeasure8'] 
                resep.strMeasure9 = d['strMeasure9'] 
                resep.strMeasure10 = d['strMeasure10'] 
                resep.strMeasure11 = d['strMeasure11'] 
                resep.strMeasure12 = d['strMeasure12'] 
                resep.strMeasure13 = d['strMeasure13'] 
                resep.strMeasure14 = d['strMeasure14'] 
                resep.strMeasure15 = d['strMeasure15'] 
                resep.strMeasure16 = d['strMeasure16'] 
                resep.strMeasure17 = d['strMeasure17'] 
                resep.strMeasure18 = d['strMeasure18'] 
                resep.strMeasure19 = d['strMeasure19'] 
                resep.strMeasure20 = d['strMeasure20'] 
                resep.save()
            else:
                Masakan.objects.create(
                    idMeal = d['idMeal'],         
                    strArea = d['strArea'], 
                    strCategory = d['strCategory'], 
                    strMeal = d['strMeal'],
                    strMealThumb = d['strMealThumb'],
                    strInstructions = d['strInstructions'],
                    strYoutube = d['strYoutube'],
                    strIngredient1 = d['strIngredient1'],
                    strIngredient2 = d['strIngredient2'], 
                    strIngredient3 = d['strIngredient3'], 
                    strIngredient4 = d['strIngredient4'],
                    strIngredient5 = d['strIngredient5'], 
                    strIngredient6 = d['strIngredient6'], 
                    strIngredient7 = d['strIngredient7'], 
                    strIngredient8 = d['strIngredient8'], 
                    strIngredient9 = d['strIngredient9'], 
                    strIngredient10 = d['strIngredient10'], 
                    strIngredient11 = d['strIngredient11'], 
                    strIngredient12 = d['strIngredient12'], 
                    strIngredient13 = d['strIngredient13'], 
                    strIngredient14 = d['strIngredient14'], 
                    strIngredient15 = d['strIngredient15'], 
                    strIngredient16 = d['strIngredient16'], 
                    strIngredient17 = d['strIngredient17'], 
                    strIngredient18 = d['strIngredient18'], 
                    strIngredient19 = d['strIngredient19'], 
                    strIngredient20 = d['strIngredient20'], 
                    strMeasure1 = d['strMeasure1'], 
                    strMeasure2 = d['strMeasure2'], 
                    strMeasure3 = d['strMeasure3'], 
                    strMeasure4 = d['strMeasure4'], 
                    strMeasure5 = d['strMeasure5'], 
                    strMeasure6 = d['strMeasure6'], 
                    strMeasure7 = d['strMeasure7'], 
                    strMeasure8 = d['strMeasure8'], 
                    strMeasure9 = d['strMeasure9'], 
                    strMeasure10 = d['strMeasure10'], 
                    strMeasure11 = d['strMeasure11'], 
                    strMeasure12 = d['strMeasure12'], 
                    strMeasure13 = d['strMeasure13'],
                    strMeasure14 = d['strMeasure14'], 
                    strMeasure15 = d['strMeasure15'], 
                    strMeasure16 = d['strMeasure16'], 
                    strMeasure17 = d['strMeasure17'], 
                    strMeasure18 = d['strMeasure18'], 
                    strMeasure19 = d['strMeasure19'], 
                    strMeasure20 = d['strMeasure20'],
                    
                )
        
    except:
        return HttpResponse("<h1>pencarian tidak di temukan</h1>")
    
    
            
    data1 = Masakan.objects.filter(strMeal__contains=search)
    
    context = {
        "data" : data1
    }
    
    return render(request, template_name, context)

def detailresep(request, id):
    
    template_name = "front/detailresep.html"
    
    data = Masakan.objects.filter(idMeal= id)
    
    space = range(20)
    
    context = {
        "data" : data   [0],
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