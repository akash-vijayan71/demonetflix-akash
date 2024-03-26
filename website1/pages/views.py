from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from . models import Contact,Register,Video,Adminlogin
from django.contrib import messages

# Create your views here.

def index(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render({},request))
def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())
def contact(request):
    if request.method=="POST":
        con_name=request.POST["con_name"]
        con_email=request.POST["con_email"]
        con_message=request.POST["con_message"]

        contact=Contact(con_name=con_name,
                        con_email=con_email,
                        con_message=con_message)
        contact.save()

    template=loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
def service(request):
    template=loader.get_template("service.html")
    return HttpResponse(template.render())
def register(request):
      if request.method=="POST":
        reg_name=request.POST["reg_name"]
        reg_email=request.POST["reg_email"]
        reg_phone=request.POST["reg_phone"]
        reg_uname=request.POST["reg_uname"]
        reg_pwd=request.POST["reg_pwd"]
        same=Register.objects.filter(reg_email=reg_email,
                                     reg_name=reg_name,
                                     reg_uname=reg_uname)
        if same:
            messages.success(request,"User already exists!")
            return HttpResponseRedirect("/register")
        else:
             register=Register(reg_name=reg_name,
                        reg_email=reg_email,
                        reg_phone=reg_phone,
                        reg_uname=reg_uname,
                        reg_pwd=reg_pwd)
        register.save()

      template=loader.get_template("register.html")
      return HttpResponse(template.render({},request))
def login(request):
    if request.method=='POST':
        log_uname=request.POST["log_uname"]
        log_pwd=request.POST["log_pwd"]

        login=Register.objects.filter(reg_uname=log_uname,reg_pwd=log_pwd)

        if login:
            request.session["user"]=log_uname
            return HttpResponseRedirect("/index")

    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))
def account(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")  
    
    template=loader.get_template("account.html")
    return HttpResponse(template.render({},request))
def logout(request):
    if 'user' in request.session:
        del request.session["user"]
    return HttpResponseRedirect("/login")
def addvideos(request):
    if request.method=='POST':
        v_name=request.POST["v_name"]
        v_video=request.FILES["v_video"]
        v_thumbnail=request.FILES["v_thumbnail"]

        video=Video(v_name=v_name,
                    v_video=v_video,
                    v_thumbnail=v_thumbnail)
        video.save()

    template=loader.get_template("addvideos.html")
    return HttpResponse(template.render({},request))
def videos(request):
    videos=Video.objects.all().values()

    context={
        'videos':videos
    }

    template=loader.get_template("videos.html")
    return HttpResponse(template.render(context,request))
def adminpage(request):
    videos=Video.objects.all().values()

    context={
        'videos':videos
    }

    template=loader.get_template("adminpage.html")
    return HttpResponse(template.render(context,request))
def adminlogin(request):
    if request.method=='POST':
        ad_uname=request.POST['ad_uname']
        ad_pwd=request.POST['ad_pwd']

        adminlogin = Adminlogin.objects.filter(
                                ad_uname=ad_uname,
                                ad_pwd=ad_pwd)
        
        if adminlogin:
            request.session["adminuser"]=ad_uname
            return HttpResponseRedirect("/adminpage")
  
    template=loader.get_template("adminlogin.html")
    return HttpResponse(template.render({},request))
def deletevideo(request,id):
    dv=Video.objects.filter(id=id)[0]
    
    dv.delete()
    return HttpResponseRedirect("/adminpage")