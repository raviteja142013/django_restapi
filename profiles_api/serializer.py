from rest_framework import serializers

class Hello_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)