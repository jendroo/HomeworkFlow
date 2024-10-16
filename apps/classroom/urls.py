from django.urls import path
from apps.classroom.views import (
    ClassEnvironmentDetailAPIView,
    LessonAPIView,
    NotificationAPIView,
    NotificationDetailAPIView,
)

app_name ='classroom-urls'
urlpatterns = [
     # GET, PUT, DELETE for a specific ClassEnvironment instance using class_id
    path("class/<int:class_id>/", ClassEnvironmentDetailAPIView.as_view(), name="classenvironment-detail"), # get specific class by id
    # POST to create a new ClassEnvironment
    path("class/create/", ClassEnvironmentDetailAPIView.as_view(), name="classenvironment-list"), # for creating classenvironment
    # Lesson views
    # Get, Update or Delete a specific lesson by lesson_id
    #path("lesson/delete/<int:lesson_id>/", LessonAPIView.as_view(), name="lesson-detail"),
    path("lesson/all/", LessonAPIView.as_view(), name="all-lessons"),
    # create new lesson
    path("lesson/create/", LessonAPIView.as_view(), name="lesson-create"),
    # Notification views
    path('notification/all/', NotificationAPIView.as_view(), name='notification-list'), # for GET, POST
    path('notification/<int:notification_id>/', NotificationDetailAPIView.as_view(), name='notification-detail'),# for GET (specific), PUT, DELETE
]