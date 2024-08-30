from common.models import Banner
from places.models import CommentImage, Comments
from rest_framework import serializers
from users.models import BookMark, CustomUser, ViewHistory


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["profile_image", "nickname", "email"]


class BookMarkSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="place.store_image")
    place_name = serializers.CharField(source="place.name")
    rating = serializers.IntegerField(source="place.rating")
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = BookMark
        fields = ["id", "bookmark", "image", "place_name", "rating", "comments_count"]

    def get_comments_count(self, obj):
        return Comments.objects.filter(place=obj.place).count()


class ViewHistorySerializer(serializers.ModelSerializer):
    bookmark = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    place_name = serializers.CharField(source="place.name")
    rating = serializers.IntegerField(source="place.rating")
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = ViewHistory
        fields = ["bookmark", "image", "place_name", "rating", "comments_count"]

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.place.store_image.url) if obj.place.store_image else None


    def get_bookmark(self, obj):
        return BookMark.objects.filter(user=obj.user, place=obj.place).exists()

    def get_comments_count(self, obj):
        return Comments.objects.filter(place=obj.place).count()


class CommentsSerializer(serializers.ModelSerializer):
    place_image = serializers.URLField(source="place.store_image")
    place_name = serializers.CharField(source="place.name")
    rating_point = serializers.IntegerField(source="rating")
    create_date = serializers.SerializerMethodField()
    comments_images = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ["id", "place_image", "place_name", "rating_point", "create_date", "content", "comments_images"]

    def get_create_date(self, obj):
        return obj.created_at.strftime("%Y.%m.%d")  # 날짜 부분만 추출


    def get_comments_images(self, obj):
        request = self.context.get("request")
        return [request.build_absolute_uri(image.image.url) for image in CommentImage.objects.filter(comment=obj)]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["image", "url_link"]
