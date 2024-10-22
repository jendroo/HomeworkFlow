from rest_framework import serializers
from ..models import Notification
from .classenvironment import ClassEnvironmentSerializer

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','name','date', 'description','class_id']