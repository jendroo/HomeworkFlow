from django.db import models
from django.contrib.auth.models import AbstractUser


roles = {
    "TEACHER": "Teacher",
    "PARENT": "Parent",
    "STUDENT": "Student",   
}

# class HomeworkflowUser(AbstractUser):
#     role = models.CharField(choices=roles, max_length=10)

class Teacher(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    main_class_id = models.IntegerField()
    role = models.CharField(choices=roles, max_length=10)  

class Parent(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    role = models.CharField(choices=roles, max_length=10)

class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    class_id = models.ForeignKey('classroom.ClassEnvironment', on_delete=models.PROTECT)
    parent_id = models.ForeignKey('userprofile.Parent', on_delete=models.SET_NULL, null=True)
    role = models.CharField(choices=roles, max_length=10)
