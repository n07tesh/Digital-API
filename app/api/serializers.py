from django.utils.translation import activate
from rest_framework import serializers
from app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

# create method for post requests 
    def create(self,validated_data):
        #this return gives the data to the views.py in post request method
        return Movie.objects.create(**validated_data)

# instanse carry old data and validated data carry new data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.discription = validated_data.get('description', instance.name)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance