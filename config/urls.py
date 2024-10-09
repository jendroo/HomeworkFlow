"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.classroom.views import (
    ClassEnvironmentDetailAPIView,
    LessonAPIView,
    NotificationAPIView,
    NotificationDetailAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    #'ClassEnvironment views'
    # GET, PUT, DELETE for a specific ClassEnvironment instance using class_id
    path("api/v1/classes/<int:class_id>/", ClassEnvironmentDetailAPIView.as_view(), name="classenvironment-detail"), # get specific class by id
    # POST to create a new ClassEnvironment
    path("api/v1/classes/", ClassEnvironmentDetailAPIView.as_view(), name="classenvironment-list"), # for creating classenvironment
    # Lesson views
    # Get, Update or Delete a specific lesson by lesson_id
    path("api/v1/lessons/<int:lesson_id>/", LessonAPIView.as_view(), name="lesson-detail"),
    # create new lesson
    path("api/v1/lessons/", LessonAPIView.as_view(), name="lesson-create"),
    # Notification views
    path('api/v1/notification/', NotificationAPIView.as_view(), name='notification-list'), # for GET, POST
    path('api/v1/notification/<int:notification_id>/', NotificationDetailAPIView.as_view(), name='notification-detail'),# for GET (specific), PUT, DELETE
]
