from django.shortcuts import render
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
    
    # def post(self, request, *args, **kwargs):
    #     data = {
    #         "lesson_id": request.data.get("lesson_id"),
    #         "due_date": request.
    #         "description":
    #     }