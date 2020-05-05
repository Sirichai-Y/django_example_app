from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Province, Message, Situation
from .serializers import ProvinceSerializer, SituationSerializer, MessageSerializer, CreateMessageSerializer

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