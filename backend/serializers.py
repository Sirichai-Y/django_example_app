from rest_framework import serializers
from .models import Province, Message, Situation, Comment

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'province_name')

class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = ('id', 'situation_name', 'situation_start')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'message_comment', 'comment_sender', 'create_at')

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message_id', 'message_comment', 'comment_sender')

class MessageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    message_situation = serializers.CharField(read_only=True)
    message_from = serializers.CharField(read_only=True)
    message_to = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = fields = (
            'id', 
            'message_sentence', 
            'message_sender', 
            'message_like', 
            'message_from', 
            'message_situation', 
            'message_to',
            'comments',
            'create_at'
        )

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
