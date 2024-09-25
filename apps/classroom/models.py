from django.db import models
from apps.userprofile.models import Teacher

# Create your models here.

school_days = {
    "Mon":"Monday",
    "Tue":"Tuesday",
    "Wed":"Wednesday",
    "Thu":"Thursday",
    "Fri":"Friday",
    "Sat":"Saturday"
}

class ClassEnvironment(models.Model):
    teacher = models.ManyToManyField('userprofile.Teacher')
    class_name = models.CharField(max_length=5)

class Lesson(models.Model):
    subject_name = models.CharField(max_length=30)
    teacher_id = models.ForeignKey('userprofile.Teacher', on_delete=models.CASCADE)
    class_id = models.OneToOneField('classroom.ClassEnvironment', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(choices=school_days, max_length=10)

class Notification(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    description = models.TextField()
    class_id = models.ForeignKey('classroom.ClassEnvironment', on_delete=models.CASCADE)