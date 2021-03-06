from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room, Chat


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ("creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
   
    user = UserSerializer()
    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Chat
        fields = ("room", "text")