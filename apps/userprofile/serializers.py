from rest_framework import serializers
from django.contrib.auth.models import User
from apps.userprofile.models import Teacher, Parent, Student
from apps.classroom.models import ClassEnvironment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

# Serializer for Teacher
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'main_class_id', 'role']

# Serializer for Parent
class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = ['user', 'role']

# Serializer for Student
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class_id = serializers.PrimaryKeyRelatedField(queryset=ClassEnvironment.objects.all())
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(), allow_null=True)

    class Meta:
        model = Student
        fields = ['user', 'class_id', 'parent_id', 'role']
