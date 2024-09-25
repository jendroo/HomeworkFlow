from django.contrib import admin
from .models import Teacher, Parent, Student
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)