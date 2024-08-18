from rest_framework import serializers
from .models import Place, ServicesIcon, PlaceImage, CommentImage, RecommendedPlace, Comments

class ServicesIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIcon
        fields = ['name', 'image']

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['image']

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = ['image']

class CommentsSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(many=True)

    class Meta:
        model = Comments
        fields = ['content', 'rating', 'comment_images']

class RecommendedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedPlace
        fields = ['place', 'content', 'tags']

class PlaceSerializer(serializers.ModelSerializer):
    service_icons = ServicesIconSerializer(many=True)
    place_images = PlaceImageSerializer(many=True)
    comments = CommentsSerializer(many=True)
    recommended_places = RecommendedPlaceSerializer(many=True)

    class Meta:
        model = Place
        fields = ['name', 'address', 'rating', 'description', 'price_text', 'service_icons', 'place_images', 'comments', 'recommended_places']
