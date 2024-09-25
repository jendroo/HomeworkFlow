from django.contrib import admin
from .models import ClassEnvironment, Lesson, Notification

# Register your models here.

admin.site.register(ClassEnvironment)
admin.site.register(Lesson)
admin.site.register(Notification)