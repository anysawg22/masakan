
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homePage, name="home"),
    path("aboutme/", aboutMe, name="aboutme"),
    path("blog/", blog, name="blog"),
    path("search/", search, name="search"),
    path("detailresep/<int:id>", detailresep, name="detailresep"),
    path("login/", loginPage, name="login"),
    path("detailblog/<int:id>", detailBlog, name="detailblog"),
    # 
    path("dashboard/", include('news.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
