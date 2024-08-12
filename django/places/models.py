from common.models import CommonModel
from users.models import CustomUser

from django.db import models


class ServicesIcon(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key, Unique Identifier
    image_url = models.URLField(max_length=255, blank=True, null=True)  # 아이콘 이미지 URL
    name = models.CharField(max_length=255, null=False)  # 정보 이름, Not Null

    def __str__(self):
        return self.name


class Place(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    store_icon = models.ForeignKey(
        ServicesIcon, on_delete=models.CASCADE, related_name="places"
    )  # Foreign Key로 StoreIcon 참조
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="places")  # Foreign Key로 User 참조
    name = models.CharField(max_length=255, null=False)  # 장소 이름, Not Null
    region = models.CharField(max_length=255, null=False)
    description = models.TextField()  # 장소 설명
    address = models.CharField(max_length=255, null=False)  # 주소, Not Null
    price_text = models.TextField(blank=True, null=True)  # 가격 텍스트, 필수 아님
    price_link = models.URLField(blank=True, null=True)  # 가격 링크, 필수 아님
    content = models.TextField(blank=True, null=True)  # 상세 내용, 필수 아님
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)  # 평점, 필수 아님
    instruction = models.CharField(max_length=50, blank=True, null=True)  # 이용 안내, 필수 아님

    def __str__(self):
        return self.name


class RecommendedPlace(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    place = models.ForeignKey(
        "Place", on_delete=models.CASCADE, related_name="recommended_places"
    )  # Foreign Key로 places 테이블 참조
    content = models.TextField(blank=True, null=True)  # 내용, 필수 아님
    tags = models.CharField(max_length=255, blank=True, null=True)  # 해쉬태그, 필수 아님

    def __str__(self):
        return self.place.name if self.place else f"Recommended Place {self.id}"

