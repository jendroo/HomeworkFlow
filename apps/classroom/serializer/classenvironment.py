from rest_framework import serializers
from ..models import ClassEnvironment
from apps.userprofile.models import Teacher

# Tevin should have TeacherSerializer defined
class TeacherSerializer(serializers.ModelSerializer):
   class Meta:
        model = Teacher
        fields = ['user', 'main_class_id']

class ClassEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassEnvironment
        fields = ['teacher', 'class_name']

  
    




        