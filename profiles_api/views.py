# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer
from rest_framework import viewsets

# Create your views here.

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializer.Hello_serializer
    def list(self,request):
        a_viewset=[
            "viewset feature 1",
            "viewset feature 2",
            "viewset feature 3",
        ]
        return Response({'message':'viewset',
                         'a_viewset': a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data  = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk = None):
        return Response({"message":"retrieve"}) 
    def update(self,request,pk = None):
        return Response({"message":"update"})
    def partial_update(self,request,pk = None):
        return Response({"message":"partial_update"})  
    def destroy(self,request,pk = None):
        return Response({"message":"destroy"})  
    

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

    def put(self,request,pk = None):
        return Response({"message":"PUT"})            

    def patch(self,request,pk = None):
        return Response({"message":"PATCH"})
    
    def delete(self,request,pk = None):
        return Response({"message":"DELETE"})
