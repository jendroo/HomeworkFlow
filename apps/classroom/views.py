from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser

from .models import ClassEnvironment, Notification, Lesson
from .serializer.classenvironment import ClassEnvironmentSerializer
from .serializer.lesson import LessonSerializer
from .serializer.notification import NotificationSerializer
from apps.userprofile.models import Teacher



# Create your views here.
class ClassEnvironmentDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    # Retrieve a specific ClassEnvironment
   
    def get(self, request, class_id, *args, **kwargs):
        class_environment = get_object_or_404(ClassEnvironment, id=class_id)

        serializer = ClassEnvironmentSerializer(class_environment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a new ClassEnvironment
    def post(self, request, *args, **kwargs):
        serializer = ClassEnvironmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing ClassEnvironment
    def put(self, request, class_id, *args, **kwargs):
        class_environment = get_object_or_404(ClassEnvironment, id=class_id)
        serializer = ClassEnvironmentSerializer(class_environment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a ClassEnvironment
    def delete(self, request, class_id, *args, **kwargs):
        try:
            class_environment = ClassEnvironment.objects.get(id=class_id)  # Using class_id here
            class_environment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ClassEnvironment.DoesNotExist:
            return Response({"error": "Class environment not found."}, status=status.HTTP_404_NOT_FOUND)
        



class LessonAPIView(APIView):
    # queryset = Lesson.objects.all()
    # serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    
    
    # def get_queryset(self):
    #     return self.queryset
    
    # def get_object(self):
    #     lesson_id = self.kwargs['pk']
    #     return self.get_queryset().filter(id=lesson_id)
    
    # def get(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #     except Lesson.DoesNotExist:
    #         return Response({"error": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

        # lesson = Lesson.objects.all()
        # serializer = LessonSerializer(lesson, many = True)
    
        # return Response(serializer.data, status=status.HTTP_200_OK)

    # GET: Retrieve a specific lesson by its ID

    def get(self, request, *args, **kwargs):
        homework = Lesson.objects.all()
        serializer = LessonSerializer(homework, many = True)
    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self, request, lesson_id, *args, **kwargs):
    #     try:
    #         lesson = get_object_or_404(Lesson, id=lesson_id)
    #     except Lesson.DoesNotExist:
    #         return Response({"error": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = LessonSerializer(lesson)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Create a new lesson


    def post(self, request, *args, **kwargs):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT: Update an existing lesson by its ID
    def put(self, request, lesson_id, *args, **kwargs):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        serializer = LessonSerializer(lesson, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a specific lesson by its ID
    def delete(self, request, lesson_id, *args, **kwargs):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.delete()
        return Response({"message": "Lesson deleted successfully."}, status=status.HTTP_204_NO_CONTENT)










class NotificationAPIView(APIView):
    """API View to manage notifications."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request to list all notifications."""

        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Handle POST request to create a new notification."""

        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificationDetailAPIView(APIView):
    """API View to retrieve, update, or delete a notification."""

    permission_classes = [IsAuthenticated]

    def get(self, request, notification_id):
        """
        Handle GET request to retrieve a specific notification.
        """
        notification = get_object_or_404(Notification, id=notification_id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, notification_id):
        """
        Handle PUT request to update an existing notification.
        """
        notification = get_object_or_404(Notification, id=notification_id)
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notification_id):
        """
        Handle DELETE request to remove a notification.
        """
        notification = get_object_or_404(Notification, id=notification_id)
        notification.delete()
        return Response({"detail": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

