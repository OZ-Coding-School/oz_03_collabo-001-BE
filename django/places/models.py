from common.models import CommonModel
from users.models import CustomUser

from django.db import models


class ServicesIcon(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key, Unique Identifier
    image = models.ImageField(upload_to="ServicesIcon_images/")
    name = models.CharField(max_length=255, null=False)  # 정보 이름, Not Null

    def __str__(self):
        return self.name


class PlaceRegion(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key, Unique Identifier
    region = models.CharField(max_length=255, null=False)  # 지역 이름, Not Null

    def __str__(self):
        return self.region


class PlaceSubcategory(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key, Unique Identifier
    subcategory = models.CharField(max_length=255, null=False)  # 카페,펜션,음식점... Not Null

    def __str__(self):
        return self.subcategory


class Place(CommonModel):
    CATEGORY_CHOICES = [
        ("펫존", "펫존"),
        ("키즈존", "키즈존"),
    ]

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    store_image = models.ImageField(upload_to="place_image/")  # 대표이미지 아이콘
    service_icons = models.ManyToManyField(ServicesIcon, related_name="places")  # ManyToManyField로 변경
    place_region = models.ManyToManyField(PlaceRegion, related_name="places")  # [서울], [경기] ....
    place_subcategory = models.ManyToManyField(PlaceSubcategory, related_name="places")  # 카페, 펜션, 음식점 ...
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="places")  # Foreign Key로 User 참조
    name = models.CharField(max_length=255, null=False)  # 장소 이름, Not Null
    description = models.TextField()  # 장소 설명
    address = models.CharField(max_length=255, null=False)  # 주소, Not Null
    price_text = models.TextField(blank=True, null=True)  # 가격 텍스트, 필수 아님
    price_link = models.URLField(blank=True, null=True)  # 가격 링크, 필수 아님
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    instruction = models.CharField(max_length=50, blank=True, null=True)  # 이용 안내, 필수 아님
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class PlaceImage(CommonModel):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="place_images"
    )  # Foreign Key로 Comment 참조
    image = models.ImageField(upload_to="place_images/")  # 이미지 파일

    def __str__(self):
        return f"Image for place ID {self.place.id}"


class PlaceDescriptionImage(CommonModel):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="place_description_images"
    )  # Foreign Key로 Comment 참조
    image = models.ImageField(upload_to="place_images/")  # 이미지 파일

    def __str__(self):
        return f"Image for place ID {self.place.id}"


class RecommendedPlace(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="recommended_places"
    )  # Foreign Key로 places 테이블 참조
    content = models.TextField(blank=True, null=True)  # 내용, 필수 아님
    tags = models.CharField(max_length=255, blank=True, null=True)  # 해쉬태그, 필수 아님

    def __str__(self):
        return self.place.name if self.place else f"Recommended Place {self.id}"


class Comments(CommonModel):
    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    id = models.BigAutoField(primary_key=True)  # Primary Key, Unique Identifier
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")  # Foreign Key로 User 참조
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")  # Foreign Key로 Place 참조
    content = models.TextField(null=False)  # 내용, Not Null
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.user.nickname} - {self.place.name}"


class CommentImage(CommonModel):
    comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name="comment_images"
    )  # Foreign Key로 Comment 참조
    image = models.ImageField(upload_to="comment_images/")  # 이미지 파일

    def __str__(self):
        return f"Image for Comment ID {self.comment.id}"
