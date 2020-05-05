from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Province, Message, Situation, Comment
from .serializers import ProvinceSerializer, SituationSerializer, MessageSerializer
from .serializers import CreateMessageSerializer, CommentSerializer, CreateCommentSerializer

@api_view(['GET'])
def province(request):
    provinces = Province.objects.all()
    serializer = ProvinceSerializer(provinces, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def situation(request):
    situation = Situation.objects.all()
    serializer = SituationSerializer(situation, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def message(request):
    if request.method == 'GET':
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        message_data = CreateMessageSerializer(data=request.data)
        if message_data.is_valid():
            message_data.save()
            return  Response(message_data.data, status=status.HTTP_201_CREATED)
        return Response(message_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def give_heart_message(request, mid):
    try:
        message = Message.objects.get(id=mid)
        heart = MessageSerializer(message).data
        heart["message_like"] += 1
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    message_data = MessageSerializer(message, data=heart)
    if message_data.is_valid():
        message_data.save()
        return  Response(message_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def manage_message(request, mid):
    try:
        message = Message.objects.get(id=mid)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        message_data = MessageSerializer(message, data=request.data)
        if message_data.is_valid():
            message_data.save()
            return  Response(message_data.data)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def message_by_province(request, prov):
    message = Message.objects.filter(message_to=prov)
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def message_by_situation(request, sit):
    message = Message.objects.filter(message_situation=sit)
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def message_by_situation_province(request, sit, prov):
    message = Message.objects.filter(message_situation=sit, message_to=prov)
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment(request):
    comment_data = CreateCommentSerializer(data=request.data)
    if comment_data.is_valid():
        comment_data.save()
        return  Response(comment_data.data, status=status.HTTP_201_CREATED)
    return Response(comment_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def manage_comment(request, cid):
    try:
        comment = Comment.objects.get(id=cid)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        comment_data = CommentSerializer(comment, data=request.data)
        if comment_data.is_valid():
            comment_data.save()
            return  Response(comment_data.data, status=status.HTTP_201_CREATED)
        return Response(comment_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)