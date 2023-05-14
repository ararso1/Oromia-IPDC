from rest_framework import serializers
from IPDC.models import Message,Notification

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'