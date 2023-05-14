from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer,NotificationSerializer
from IPDC.models import *
from django.http import HttpResponse
from django.db.models import Q

#django restframe work

@api_view(['GET'])
def getmessages(request):
    messages=Message.objects.all()
    serializer = MessageSerializer(messages,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getunreadmessages(request,pk):
    user=User.objects.get(id=pk)
    messages=Message.objects.filter(privatechat__primary_user = user).filter(~Q(written_by =user)).filter(seen=False)
    serializer = MessageSerializer(messages,many=True)
    return Response(serializer.data)







@api_view(['GET'])
def getroommessages(request,pk):
    privateroom=Privatechat.objects.get(id=pk)
    messages=Message.objects.filter(privatechat=privateroom)
    serializer = MessageSerializer(messages,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_unseen_notifiaction(request,pk):
    user=User.objects.get(id=pk)
    unseen_notifications=Notification.objects.filter(user=user).filter(seen=False)
    serializer = NotificationSerializer(unseen_notifications,many=True)
    return Response(serializer.data)









@api_view(['POST'])
def addmessage(request):
    print("there is a request")
    serializer = MessageSerializer(data=request.data)
    print("my request IC",request.data)
    if serializer.is_valid():
        print("it is working")
        serializer.save()
    else:
        return HttpResponse("notworking")
    return Response(serializer.data)
