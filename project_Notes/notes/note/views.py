from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse , request
from django.views.generic import View,FormView
from note.forms import ValidateFrm
from django.forms import forms
from .models import *

class Validfrm(View):
    def get(self,request,*args):
        return render(request,"note/newaccount.html")
    def post(self,request,*args):
        form=ValidateFrm(request.POST)
        if form.is_valid():
            userFullname=request.POST['fullname']
            userEmail=request.POST['email']
            userPass=request.POST['password']
            oobj=Users.objects.filter(Email=userEmail).exists()
            if oobj:
                return render(request,"note/newaccount.html",{'msg':'Account allready exists'})
            else:
                new_obj = Users(Name=userFullname,Email=userEmail,Password=userPass)
                new_obj.save()
                return render(request,"note/newaccount.html",{'msgs':'Registered'})
        else:
            return render(request,"note/newaccount.html",{'form':form})
def index(request, msg=""):
    if msg is not None:
        return render(request,"note/index.html",{'msg':msg})
    else:
        return render(request,"note/index.html")
def user_home(request):
    user = request.session['USER']
    user_data = Users.objects.get(Email=user)
    notes = Note.objects.filter(User_id_id=user_data.id)
    return render(request,"note/home.html",{'user':user_data.id,'note':notes})
def log(request):
    if request.method == 'POST':
        Umail = request.POST['email']
        Upass = request.POST['pwd']
        new_obj=Users.objects.filter(Email=Umail).exists()
        if new_obj:
            try:
                user_data = Users.objects.get(Email=Umail,Password=Upass)
                request.session['USER']=user_data.Email
                notes = Note.objects.filter(User_id_id=user_data.id)
                return render(request,"note/home.html",{'user': user_data.id,'note':notes})
            except Exception as e:
                msg = 'Incorrect Password.'
                return index(request,msg)
        else:
            msg ='Email not Registered.'
            return index(request,msg)
    else:
        return index(request)
def logout(request):
    del request.session['USER']
    return index(request)
def add_note(request, id):
    if request.method == 'POST':
        nt = request.POST['note_title']
        nst = request.POST['note_subtitle']
        ntext = request.POST['note_text']
        new_obj = Note(Title=nt,Subtitle=nst,Description=ntext,User_id_id=id)
        new_obj.save()
        return redirect("user_home/")
    return HttpResponse("fail")
def edit_note(request, id):
    user = request.session['USER']
    user_data = Users.objects.get(Email=user)
    new = Note.objects.filter(id=id)
    return render(request,"note/edit.html",{'user': user_data.id,'s':new})
def save_note(request, id):
    if request.method == 'POST':
        n=Note.objects.get(id=id)
        n.Title = request.POST['note_title']
        n.Subtitle = request.POST['note_subtitle']
        n.Description = request.POST['note_text']
        n.save()
        return redirect("user_home/")
    return user_home(request)
def del_note(request, id):
    if request.session._session:
        n=Note.objects.get(id=id)
        n.delete()
        return redirect("user_home/")
    else:
        return HttpResponse("<strong>User not Exist</strong>")
