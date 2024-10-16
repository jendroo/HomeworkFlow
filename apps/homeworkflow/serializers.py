from rest_framework import serializers
from .models import Absence, Homework, Homework_Uncompleted, Weekly_Feedback

class AbsenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence
        fields = ["date", "student", "type", "lesson"]

class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ["lesson_id", "due_date", "description"]

class HomeworkUncompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework_Uncompleted
        fields = ["homework", "student"]

class WeeklyFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weekly_Feedback
        fields = [
            "student", 
            "teacher", 
            "written_feedback",
            "social_behaviour",
            "work_ethics",
                    ]


