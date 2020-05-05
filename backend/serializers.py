from rest_framework import serializers
from .models import Province, Message, Situation

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'province_name')

class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = ('id', 'situation_name', 'situation_start')

class MessageSerializer(serializers.ModelSerializer):
    message_situation = serializers.CharField(read_only=True)
    message_from = serializers.CharField(read_only=True)
    message_to = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id', 
            'message_sentence', 
            'message_sender', 
            'message_like', 
            'message_from', 
            'message_situation', 
            'message_to'
        )
