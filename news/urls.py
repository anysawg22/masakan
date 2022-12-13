from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("tablenews/", seeNews, name="tablenews"),
    path("addnews/", addNews, name="addnews"),
    path("editnews/<int:id>", editNews, name="editnews"),
    path("deletenews/<int:id>", deleteNews, name="deletenews"),
    path("register/", register, name="register"),
    path("edituser/<int:id>", editUser, name="edituser"),
    path("deleteuser/<int:id>", hapusUsers, name="hapususer"),
    path("logout/", logoutPage, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)