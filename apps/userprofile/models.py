from django.db import models
import django.contrib.auth
from django.contrib.auth.models import AbstractUser

roles = {
    "TEACHER": "Teacher",
    "PARENT": "Parent",
    "STUDENT": "Student",   
}

# class HomeworkflowUser(AbstractUser):
#     role = models.CharField(choices=roles, max_length=10)

class User(AbstractUser):
    role = models.CharField(choices=roles, max_length=10)

    def __str__(self):
        
        return f'{self.username} - {self.first_name} {self.last_name} {self.role}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main_class_id = models.IntegerField()
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # def __str__(self):
    #     teachername = self.request.user.get_full_name()
    #     return f'{teachername}{self.role}' 

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classenvironment = models.ForeignKey('classroom.ClassEnvironment', on_delete=models.PROTECT)
    parent = models.ForeignKey('userprofile.Parent', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
