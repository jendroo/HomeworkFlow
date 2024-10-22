from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Absence, Homework, Homework_Uncompleted, Weekly_Feedback
from .serializers import AbsenceSerializer, HomeworkSerializer, HomeworkUncompletedSerializer, WeeklyFeedbackSerializer



# Create your views here.

class HomeworkApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        homework = Homework.objects.all()
        serializer = HomeworkSerializer(homework, many = True)
    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            "lesson_id": request.data.get("lesson_id"),
            "due_date": request.data.get("due_date"),
            "description": request.data.get("description")
        }

        serializer = HomeworkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AbsenceApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            "date": request.data.get("date"),
            "student": request.data.get("student"),
            "type":request.data.get("type"),
            "lesson":request.data.get("lesson")
        }
        
        serializer = AbsenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HomeworkMissingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            "homework": request.data.get("homework"),
            "student": request.data.get("student"),
           
        }
        
        serializer = HomeworkUncompletedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WeeklyFeedbackApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            "student":request.data.get("student"),
            "teacher":request.data.get("teacher"),
            "written_feedback":request.data.get("written_feedback"),
            "social_behaviour":request.data.get("social_behaviour"),
            "work_ethics":request.data.get("work_ethics")
        }

        serializer = WeeklyFeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        feedback = get_object_or_404(Weekly_Feedback, id=id)
        data = {
            "parent_checked":request.data.get("parent_checked")
        }
        serializer = WeeklyFeedbackSerializer(feedback, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    