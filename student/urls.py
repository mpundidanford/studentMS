
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.Homepage),
    path('', views.loginpage),
    path('dologin', views.dologin),
    # path('getUserDetail', views.getUserDetails),
    path('logout', views.logout),
    path('adminHome', views.adminHome),
    path('add_staff', views.addStaff),
    path('add_staff_save', views.add_staff_save), 
    path('add_course', views.addCourse),
    path('add_course_save', views.add_course_save),
    path('add_student', views.addStudent),
    path('add_student_save', views.add_student_save)
]
