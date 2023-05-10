from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from schapp.models import Course
from schapp.models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')
def admpage(request):
    return render(request,'admpage.html') 
def addc(request):
    return render(request,'addcourse.html')
   


def adds(request):
   courses=Course.objects.all()
   return render(request,'addstudent.html',{'course':courses})
def addcdb(request):
    if request.method=="POST":
        course_name=request.POST.get('course_name')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('/')
def addsdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('/')   
def login1(request):
 if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username, password=password) 
    #request.session["uid"]=user.id#session method part
    if user is not None:
        if user.is_staff:
            login(request,user)
            return redirect('admpage')
        else:
            login(request,user)
            auth.login(request,user)
            messages.info(request,f'Welcome{username}')
            return redirect('home')
        
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('home')
 else:
     return redirect('home')