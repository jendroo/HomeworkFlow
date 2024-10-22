from rest_framework import serializers
from ..models import Lesson, ClassEnvironment
from .classenvironment import TeacherSerializer, ClassEnvironmentSerializer




class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id','subject_name', 'teacher', 'classenvironment', 'start_time', 'end_time', 'day']