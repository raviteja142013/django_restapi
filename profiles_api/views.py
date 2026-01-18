# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer


# Create your views here.
class HelloApiView(APIView):
    serializer_class = serializer.Hello_serializer
    def get(self,request,format = None):
        as_apiview =[
            'feature1',
            'feature2',
            'feature3',
            'feature4',
        ]

        return Response({'message':"Hello",
                         "an_apiview": as_apiview})


    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            # serializer.save()
            name = serializer.validated_data.get('name')
            message =f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
