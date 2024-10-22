from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.userprofile.models import Teacher, Parent, Student
from apps.classroom.models import ClassEnvironment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

# Serializer for Teacher
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'main_class_id',]


# Serializer for Parent
class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = ['user',]

# Serializer for Student
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    classenvironment = serializers.PrimaryKeyRelatedField(queryset=ClassEnvironment.objects.all())
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(), allow_null=True)

    class Meta:
        model = Student
        fields = ['user', 'classenvironment', 'parent_id',]