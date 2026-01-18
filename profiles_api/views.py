# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self,request,format = None):
        as_apiview =[
            'feature1',
            'feature2',
            'feature3',
            'feature4',
        ]

        return Response({'message':"Hello",
                         "an_apiview": as_apiview})
# Create your views here.
