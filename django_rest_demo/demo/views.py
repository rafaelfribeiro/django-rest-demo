from http import client
from rest_framework import serializers
from rest_framework.response import Response
from .models import ClientUser
from .serializers import ClientSerializer
from rest_framework.decorators import  api_view

@api_view(['GET'])
def client_list(request):
    clients = ClientUser.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def client_detail(request, pk):
    clients = ClientUser.objects.get(id=pk)
    serializer = ClientSerializer(clients, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def client_create(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def client_update(request, pk):
    client = ClientUser.objects.get(id=pk)
    serializer = ClientSerializer(instance=client, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def client_delete(request, pk):
    client = ClientUser.objects.get(id=pk)
    client.delete()

    return Response('Deleted')