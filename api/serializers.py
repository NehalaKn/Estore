from rest_framework import serializers
from api.models import Reviews

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    quantity=serializers.IntegerField()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        exclude=("created_date",)


