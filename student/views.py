
from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
from student.EmailBackend import EmailBackend
from student.models import CustomUser, staffs, Courses, Students, Subjects
from django.contrib import messages


# Create your views here.
def Homepage(request):
    return render(request, 'student/homepage.html')

def loginpage(request):
    return render(request, 'student/login.html')

def dologin(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        user =EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            # login(request,user)
            return HttpResponseRedirect('/adminHome')
            # return HttpResponse("email :"+request.POST.get("email")+"passwod :" +request.POST.get("password"))
        else:
            return HttpResponse("invalid login")
            
            
        
# def getUserDetails(request):
#     if user!=None:
#         return HttpResponse("User "+request.user.email+"Usertype"+str(request.user.user_type))
#     else:
#         return HttpResponse("login first")
    
def logout(request):
        logout(request)
        return HttpResponseRedirect('/')
 
 
    #    ADMIN MANAGEMENT SESSION    
    
def adminHome(request):
    return render(request, 'student/HoD_template/home_content.html')     

def addStaff(request):
    return render(request, 'student/HoD_template/add_staff.html')  

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("methode note allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")   
        username = request.POST.get("username")   
        email = request.POST.get("email")   
        password = request.POST.get("password")   
        address = request.POST.get("address")   
        try:
            user= CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email= email, password=password,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request, "successfull staff added")
            return HttpResponseRedirect("/add_staff")
        except: 
            messages.error(request, "failed to add") 
            return HttpResponseRedirect("/add_staff")

            
def addCourse(request):
    return render(request, "student/HoD_template/add_course.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("method not allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"successfull course added")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "cyo poa")
            return HttpResponseRedirect("/add_course")

def addStudent(request):
    courses = Courses.objects.all()
    return render(request , "student/HoD_template/add_student.html", {"courses" : courses})           
        
def add_student_save(request):
    if request.method!= "POST":
        return HttpResponseRedirect("method not allowed") 
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")   
        username=request.POST.get("username")   
        email=request.POST.get("email")   
        password=request.POST.get("password")   
        address=request.POST.get("address")
        session_start=request.POST.get("sesion_start")
        session_end=request.POST.get("sesion_end") 
        course_id=request.POST.get("course") 
        sex=request.POST.get("sex")
        try:
            user=CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email= email, password=password,user_type=3)
            user.Students.address=address
            course_obj = request.POST.get(id=course_id)
            user.Students.course_id=course_obj
            user.Students.session_start_year=session_start
            user.Students.session_end_year=session_end
            user.Students.gender=sex
            user.Students.profile_pic=""
            user.save()
            messages.success(request, "successfull student added")
            return HttpResponseRedirect("/add_student")
        except: 
            messages.error(request, "failed to add") 
            return HttpResponseRedirect("/add_student")

         
def addSubject(request):
    staffs = CustomUser.objects.all()
    courses = Courses.objects.all()
    return render(request, "student/HoD_template/add_subject.html", {"staffs": staffs, "Courses": courses})  

def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed')
    else:
        subject_name = request.POST.get("subject_name")
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        course_id= request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        try:
            Subject = Subjects(subject_name=subject_name, staffs_id=staff, course_id= course)
            Subject.save() 
            messages.success(request, "successfull subject added")
            return HttpResponseRedirect("/add_subject")
        except: 
            messages.error(request, "failed to add") 
            return HttpResponseRedirect("/add_subject")   
        
def manageStaff(request):
    staffs = CustomUser.objects.all()
    return render(request, "student/HoD_template/manage_staff.html", {"staffs": staffs})        