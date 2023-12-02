from django.shortcuts import render,redirect
from App1.models import customer
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'home.html')
def adminhome(request):
    return render(request,'adminhome.html')
def userhome(request):
    return render(request,'userhome.html')

def loginp(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['password']
        au=authenticate(username=u,password=p)
        print(au)
        request.session["user_id"]=u
        if au is not None and au.is_superuser==1:
            return render(request,"adminhome.html")
        elif au is not None and au.is_superuser==0:
            return render(request,"userhome.html")
        else:
            return HttpResponse('invalid user')
    return render(request,'login.html')


def userReg(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['pswd']
        c=request.POST['fname']
        d=request.POST['lname']
        e=request.POST['place']
        f=request.POST['phone']
        g=request.POST['email']
        p=customer(Username=a,Password=b,Firstname=c,Lastname=d,Place=e,Phone=f,Email=g)
        data=User(username=a)
        data.set_password(b)
        data.save()
        p.save()
        return HttpResponse('<script>alert("Successfully registerd"),window.location="/";</script>')
        
    return render(request,'userReg.html')

def adminDishes(request):
    return render(request,'adminDishes.html')

def adminTable(request):
    return render(request,'adminTable.html')

def viewUsers(request):
    return render(request,'viewUser.html')

def adminlogOut(request):
    logout(request)   
    return redirect('/')

# def editProfile(request):
#     return render(request,'viewUser.html')
def viewUsers(request):
    data=customer.objects.all()
    return render(request,'viewUser.html',{'x':data})
def update(request):
    id=request.session['user_id']
    data1=customer.objects.get(Username=id)
    if request.method=='POST':
        data1.Username=request.POST['username']
        data1.Password=request.POST['pswd']
        data1.Firstname=request.POST['fname']
        data1.Lastname=request.POST['lname']
        data1.Place=request.POST['place']
        data1.Phone=request.POST['phone']
        data1.Email=request.POST['email']
        data1.save()
        return HttpResponse('<script>alert("Successfully updated"),window.location="/userhome";</script>')
    return render(request,'viewUser.html',{'y':data1})

def userviewDishes(request):
    return render(request,'userviewDishes.html')

def reserveTable(request):
    return render(request,'userviewTable.html')



