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

school_subjects = {
    "Math":"Math",
    "German":"German",
    "Eng":"English",
    "Bio":"Biology",
    "Chem":"Chemistry",
    "PE":"Physical Education",
    "HST":"History",
    "Art":"Art",
    "Geo":"Geography",
    "Phi":"Philosophy",
    "Eth":"Ethics",
    "Rel":"Religion",
    "Spa":"Spanish",
    "Fre":"French",
    "Lat":"Latin",
}

class ClassEnvironment(models.Model):
    teacher = models.ManyToManyField('userprofile.Teacher')
    class_name = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.class_name}'

class Lesson(models.Model):
    subject_name = models.CharField(max_length=30, choices=school_subjects)
    teacher = models.ForeignKey('userprofile.Teacher', on_delete=models.CASCADE)
    classenvironment = models.ForeignKey('classroom.ClassEnvironment', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(choices=school_days, max_length=10)

    def __str__(self):
        return f'{self.start_time} - {self.end_time} {self.subject_name}: {self.teacher}'

class Notification(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    description = models.TextField()
    class_id = models.ForeignKey('classroom.ClassEnvironment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.date}'