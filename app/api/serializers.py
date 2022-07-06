# from dataclasses import fields
# from django.utils.translation import activate
from rest_framework import serializers
from app.models import WatchList , StreamPlatform, Review

'''
serializer validation
1.field level validation
2.object level validation
3.validator validation
'''
'''
core arguments
``
'''

'''
Model Serializer
'''
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id','name','description']
        # exclude = ['active']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(
        many=True,
        read_only=True,
        )
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie_detail'
    # )
    # watchlist = serializers.StringRelatedField(many=True) # return title

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self,object):
    #     return len(object.name)

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    # def validate(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value



















# def name_length(value):
#     if len(value)< 2:
#         raise serializers.ValidationError("Name is too short!")




# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

# # create method for post requests
#     def create(self,validated_data):
#         #this return gives the data to the views.py in post request method
#         return Movie.objects.create(**validated_data)

# # instanse carry old data and validated data carry new data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.discription = validated_data.get('description', instance.name)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different")
#         else:
#             return data

    # def validate_name(self,value):
    #     if len(value)< 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
