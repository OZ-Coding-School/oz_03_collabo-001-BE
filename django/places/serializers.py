from common.models import Banner
from rest_framework import serializers
from users.models import BookMark

from .models import (
    CommentImage,
    Comments,
    Place,
    PlaceDescriptionImage,
    PlaceImage,
    PlaceRegion,
    PlaceSubcategory,
    RecommendCategory,
    RecommendedPlace,
    RecommendTags,
    ServicesIcon,
)


class PlaceSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceSubcategory
        fields = ["id", "subcategory"]


class MainPagePlaceSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ["id", "store_image", "is_bookmarked", "place_region", "name", "address", "rating", "comments_count"]

    def get_comments_count(self, obj):
        user = self.context["request"].user
        return Comments.objects.filter(place=obj).count()

    def get_is_bookmarked(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return BookMark.objects.filter(user=user, place=obj).exists()
        return False  # 로그인하지 않았을 때는 북마크 상태를 false로 반환


class MainPageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["id", "image", "url_link"]


class MainPageRecommendedPlaceSerializer(serializers.ModelSerializer):
    places = MainPagePlaceSerializer(source="place", read_only=True)

    class Meta:
        model = RecommendedPlace
        fields = ["id", "content", "tags", "places"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Customize the representation if needed
        return representation


class ServicesIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIcon
        fields = ["name", "image"]


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ["image"]


class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = ["image"]


class CommentsSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comments
        fields = ["content", "rating", "comment_images"]


class RecommendCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendCategory
        fields = ["name"]


class RecommendTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendTags
        fields = ["id", "tag"]


class PlaceRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceRegion
        fields = ["id", "region"]


class PlaceSerializer(serializers.ModelSerializer):
    service_icons = ServicesIconSerializer(many=True)
    place_images = PlaceImageSerializer(many=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Place
        fields = [
            "name",
            "address",
            "place_region",
            "rating",
            "price_text",
            "service_icons",
            "place_images",
            "comments",
        ]


class RecommendedPlaceSerializer(serializers.ModelSerializer):
    category = RecommendCategorySerializer()
    tags = RecommendTagsSerializer(many=True, read_only=True)
    place = PlaceSerializer()

    class Meta:
        model = RecommendedPlace
        fields = ["place", "content", "category", "tags"]


class PlaceDescriptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceDescriptionImage
        fields = ["image"]  # Assuming PlaceDescriptionImage model has an image_url field


class PlaceDetailCommentsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ["user", "content", "rating", "images"]  # Adjust fields as per your model

    def get_images(self, obj):
        # Fetch the first 2 images related to this comment
        images = CommentImage.objects.filter(comment=obj)[:3]
        return CommentImageSerializer(images, many=True).data


class PlaceFullDetailCommentsSerializer(serializers.ModelSerializer):
    images = CommentImageSerializer(many=True, read_only=True, source="comment_images")

    class Meta:
        model = Comments
        fields = ["user", "content", "rating", "images"]  # Adjust fields as per your model

    def create(self, validated_data):
        user = self.context["user"]
        place_id = self.context["place"]
        place = Place.objects.get(id=place_id)

        # Remove 'user' from validated_data to avoid duplication
        validated_data.pop("user", None)

        comment = Comments.objects.create(place=place, user=user, **validated_data)
        return comment


class AegaPlaceDetailSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(source="place_images", many=True, read_only=True)
    bookmark = serializers.SerializerMethodField()
    service_icons = ServicesIconSerializer(many=True, read_only=True)
    description_images = serializers.SerializerMethodField()
    comment_images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = [
            "images",
            "bookmark",
            "store_image",
            "name",
            "address",
            "rating",
            "description_tags",
            "price_text",
            "address",
            "service_icons",
            "description_images",
            "comment_images",
            "comments_count",
            "comments",
            "instruction",
        ]

    def get_comments_count(self, obj):
        return Comments.objects.filter(place=obj).count()

    def get_description_images(self, obj):
        # Filter PlaceDescriptionImage based on the current place
        description_images = PlaceDescriptionImage.objects.filter(place=obj)
        return PlaceDescriptionImageSerializer(description_images, many=True).data

    def get_comment_images(self, obj):
        # Filter CommentImage based on comments related to the current place
        comment_images = CommentImage.objects.filter(comment__place=obj)[:3]
        return CommentImageSerializer(comment_images, many=True).data

    def get_comments(self, obj):
        # Filter Comments based on the current place
        comments = Comments.objects.filter(place=obj)[:3]
        return PlaceDetailCommentsSerializer(comments, many=True).data

    def get_bookmark(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return BookMark.objects.filter(user=user, place=obj).exists()
        return False  # 로그인하지 않았을 때는 북마크 상태를 false로 반환
