from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("service",views.service,name="service"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("account",views.account,name="account"),
    path("addvideos",views.addvideos,name="addvideos"),
    path("videos",views.videos,name="videos"),
    path("adminpage",views.adminpage,name="adminpage"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("deletevideo/<int:id>",views.deletevideo,name="deletevideo"),
    
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)