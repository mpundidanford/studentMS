from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data= ((1, "AdminHOD"), (2, "staffs"), (3,"student"))
    user_type = models.CharField(default=1, choices=user_type_data,max_length=10)
    
class AdminHoD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()
    
class staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address= models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()
    
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()
    
    
class Students(models.Model):
    id= models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses,on_delete=models.DO_NOTHING,default=1)
    gender = models.CharField(max_length=10)
    profile_pic =models.FileField()
    session_start = models.DateField()
    session_end = models.DateField()
    address = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)  
    objects= models.Manager()  
    
    
class attendece_report(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
                
    

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE, default=1)
    staffs_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class attendece(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    subject_id = models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()   
    
class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date = models.DateTimeField(auto_now_add=True)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()
    
class LeaveReportStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staffs_id = models.ForeignKey(staffs,on_delete=models.CASCADE)
    leave_date = models.DateTimeField(auto_now_add=True)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()    
    
         
class FeedbackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedbackReplay= models.TextField()
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()  
    
class FeedbackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staffs_id = models.ForeignKey(staffs,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedbackReplay = models.TextField()
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()        

    
class NotificationStudents(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    message = models.TextField()
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager() 
    
class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staffs_id = models.ForeignKey(staffs,on_delete=models.CASCADE)
    message = models.TextField()
    Created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects= models.Manager()       
    
    
@receiver(post_save,sender=CustomUser)
def Create_user_profile(sender,instance,created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminHoD.objects.create(admin=instance)
        if instance.user_type==2:
            staffs.objects.create(admin=instance, address="")
        if instance.user_type==3:
            Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_start='2020-1-1', session_end='2021-1-1',profile_pic="", gender="")            
            
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.AdminHoD.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.student.save()                        