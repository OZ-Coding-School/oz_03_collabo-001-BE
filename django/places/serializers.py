from rest_framework import serializers
from .models import Place, PlaceImage, CommentImage, ServicesIcon, Comments

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image']

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = ['id', 'image']

class CommentSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'content', 'rating', 'comment_images']

class ServicesIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIcon
        fields = ['id', 'name', 'image']

class PlaceSerializer(serializers.ModelSerializer):
    place_images = PlaceImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    service_icons = ServicesIconSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'address', 'rating', 'description', 'price_text',
            'place_images', 'comments', 'service_icons'
        ]
