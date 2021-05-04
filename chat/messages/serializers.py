from rest_framework import serializers
from .models import Message
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nombres', 'apellidos', 'username')

class MessageListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ('id','text', 'user')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'user')


