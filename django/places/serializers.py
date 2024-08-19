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


from rest_framework import serializers
from .models import RecommendedPlace, RecommendCategory, RecommendTags, Place, PlaceRegion

class RecommendCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendCategory
        fields = ['name']

class RecommendTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendTags
        fields = ['id', 'tag']

class PlaceRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceRegion
        fields = ['region']



class PlaceSerializer(serializers.ModelSerializer):
    service_icons = ServicesIconSerializer(many=True)
    place_images = PlaceImageSerializer(many=True)
    comments = CommentsSerializer(many=True)

    
    class Meta:
        model = Place
        fields = ['name', 'address', 'place_region', 'rating', 'description', 'price_text', 'service_icons', 'place_images', 'comments']


class RecommendedPlaceSerializer(serializers.ModelSerializer):
    category = RecommendCategorySerializer()
    tags = RecommendTagsSerializer(many=True, read_only=True)
    place = PlaceSerializer()

    class Meta:
        model = RecommendedPlace
        fields = ['place', 'content', 'category', 'tags']
