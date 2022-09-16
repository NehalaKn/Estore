from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    quantity=serializers.IntegerField()