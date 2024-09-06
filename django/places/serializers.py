from common.models import Banner
from rest_framework import serializers
from users.models import BookMark
from users.serializers import UserProfileSerializer

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
    store_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Place
        fields = [
            "id",
            "store_image",
            "is_bookmarked",
            "place_region",
            "place_subcategory",
            "name",
            "address",
            "rating",
            "comments_count",
        ]

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
    tags = serializers.SerializerMethodField()

    class Meta:
        model = RecommendedPlace
        fields = ["id", "content", "tags", "places"]

    def get_tags(self, obj):
        return [tag.tag for tag in obj.tags.all()]


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
        fields = ["image", "created_at", "updated_at"]


class CommentsSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(many=True, read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ["user", "content", "rating", "comment_images", "created_at", "updated_at"]


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
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = [
            "user",
            "id",
            "content",
            "rating",
            "images",
            "created_at",
            "updated_at",
        ]

    def get_images(self, obj):
        # Assuming `CommentImage` has a field `image` that stores the image file
        return [
            {
                "image": self._get_full_image_url(image.image.url),
                "created_at": image.created_at,
                "updated_at": image.updated_at,
            }
            for image in obj.comment_images.all()
        ]

    def _get_full_image_url(self, url):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(url)
        return url


class PlaceFullDetailCommentsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = [
            "user",
            "id",
            "content",
            "rating",
            "images",
            "created_at",
            "updated_at",
        ]

    def get_images(self, obj):
        request = self.context.get("request")
        images_data = []
        for image in obj.comment_images.all():
            image_url = image.image.url
            if request:
                image_url = request.build_absolute_uri(image_url)
            images_data.append(
                {
                    "url": image_url,
                    "created_at": image.created_at,
                    "updated_at": image.updated_at,
                }
            )
        return images_data

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
            "price_link",
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
        description_images = PlaceDescriptionImage.objects.filter(place=obj)
        return [self._get_full_image_url(image.image.url) for image in description_images]

    def get_comment_images(self, obj):
        comment_images = CommentImage.objects.filter(comment__place=obj)[:3]
        return [self._get_full_image_url(image.image.url) for image in comment_images]

    def get_comments(self, obj):
        comments = Comments.objects.filter(place=obj)[:3]
        return PlaceDetailCommentsSerializer(comments, many=True, context=self.context).data

    def get_bookmark(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return BookMark.objects.filter(user=user, place=obj).exists()
        return False

    def _get_full_image_url(self, url):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(url)
        return url
