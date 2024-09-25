from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.classroom.models import ClassEnvironment

roles = {
    "TEACHER": "Teacher",
    "PARENT": "Parent",
    "STUDENT": "Student",   
}

class HomeworkflowUser(AbstractUser):
    role = models.CharField(choices=roles, max_length=10)

class Teacher(models.Model):
    user = models.OneToOneField(HomeworkflowUser, on_delete=models.CASCADE)
    main_class_id = models.IntegerField()
    

class Parent(models.Model):
    user = models.OneToOneField(HomeworkflowUser, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(HomeworkflowUser, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassEnvironment, on_delete=models.PROTECT)
    parent_id = models.ForeignKey(Parent)
