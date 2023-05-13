from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from schapp.models import Course
from schapp.models import Student
from schapp.models import Usermember
import os
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required(login_url='login1')#(login_required method part)
def admpage(request):
    return render(request,'admpage.html')
@login_required(login_url='login1')#(login_required method part) 
def addc(request):
    return render(request,'addcourse.html')
   

@login_required(login_url='login1')#(login_required method part)
def adds(request):
   courses=Course.objects.all()
   return render(request,'addstudent.html',{'course':courses})
@login_required(login_url='loginpage')#(login_required method part)
def addcdb(request):
    if request.method=="POST":
        course_name=request.POST.get('course_name')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('addc')
@login_required(login_url='login1')#(login_required method part)    
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
        return redirect('adds')
      
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
            return redirect('uhome')
        
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('home')
 else:
     return redirect('home')
@login_required(login_url='login1')#(login_required method part) 
def show(request):
    
        student=Student.objects.all()
        return render(request,'showstudent.html',{'students':student})
@login_required(login_url='login1')#(login_required method part)
def edit(request,pk):
    student=Student.objects.get(id=pk)
    courses=Course.objects.all()
    return render(request,'editstudent.html',{'student':student,'course1':courses})
@login_required(login_url='login1')#(login_required method part)
def editdb(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['name']
        
        student.student_address=request.POST['address']
        
        student.student_age=request.POST['age']
        
        student.joining_date=request.POST['jdate']
        
        sel=request.POST['sel']
      
        course1=Course.objects.get(id=sel)
        
        student.course=course1
        student.save()
        return redirect('show')  
    return render(request,'editstudent.html')
@login_required(login_url='login1')#(login_required method part)
def deletepage(request,pk):
    emp=Student.objects.get(id=pk)
    emp.delete()
    return redirect('show')
@login_required(login_url='login1')#(login_required method part)
def logout(request):
    #if request.user.is_authenticated:(is authenticated method part)
    #request.session["uid"] = ""#session method part
    auth.logout(request)
    return redirect('home')

def treg(request):
    courses=Course.objects.all()
    return render(request,'teacherreg.html',{'course':courses})
def tregdb(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname') 
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        address=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('email')
        number=request.POST.get('number')
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        image=request.FILES.get('file')
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This username already exists !!!')
                return redirect('treg')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
                user.save()
                u=User.objects.get(id=user.id)

                member=Usermember(address=address,age=age,number=number,image=image,user=u,course=course1)
                member.save()

                return redirect('/')
        else:
            messages.info(request,'Password does match !!!')
            return redirect('treg')
    else:
        return render(request,'teacherreg.html')
@login_required(login_url='login1')#(login_required method part) 
def showt(request):
    
    teacher=Usermember.objects.all()
    return render(request,'showteacher.html',{'teachers':teacher})
@login_required(login_url='login1')#(login_required method part)
def deletet(request,pk):
    empl=Usermember.objects.get(user=pk)
    use=User.objects.get(id=pk)
    use.delete()
    empl.delete()
    return redirect('showt')
@login_required(login_url='login1')#(login_required method part)
def uhome(request):
    return render(request,'userhome.html')
@login_required(login_url='login1')#(login_required method part)
def seepr(request):
    current_user=request.user.id
    user1=Usermember.objects.get(user_id=current_user)
    return render(request,'seeprofile.html',{'users':user1})
@login_required(login_url='login1')#(login_required method part)
def editt(request):
        current_user= request.user.id
        print(current_user)
        user1=Usermember.objects.get(user_id=current_user)
        user2=User.objects.get(id=current_user)
        if request.method=="POST":
            if len(request.FILES)!=0:
                if len(user1.image)>0:
                 os.remove(user1.image.path)
                user1.image=request.FILES.get('file')
            user2.first_name=request.POST.get('fname')
            user2.last_name=request.POST.get('lname')
            user2.first_name=request.POST.get('fname')
            user2.username=request.POST.get('uname')
            user2.password=request.POST.get('password')
            user2.email=request.POST.get('email')
            user1.age=request.POST.get('age')
            user1.address=request.POST.get('address')
            user1.number=request.POST.get('number')
            user1.save()
            user2.save()
            return redirect('seepr')
    
        return render(request,'edit.html',{'users':user1})
    
