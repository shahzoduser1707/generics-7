from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PhoneSerializers
from .models import PhoneModel
from rest_framework import generics
# Create your views here.

class GetPhone(generics.ListAPIView):
      queryset = PhoneModel.objects.all()
      serializer_class = PhoneSerializers

class CreatePhone(generics.CreateAPIView):
      queryset = PhoneModel.objects.all()
      serializer_class = PhoneSerializers
    
class GetCreatePhone(generics.ListCreateAPIView):
      queryset = PhoneModel.objects.all()
      serializer_class = PhoneSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = PhoneModel.objects.all()
      serializer_class = PhoneSerializers