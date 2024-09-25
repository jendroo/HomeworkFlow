from django.contrib import admin
from .models import Attendance, Homework, Homework_Uncompleted, Weekly_Feedback
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Homework)
admin.site.register(Homework_Uncompleted)
admin.site.register(Weekly_Feedback)