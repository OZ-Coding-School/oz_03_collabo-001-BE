from django.db import models


# 공통 사용 모델클레스
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # 해당 object 생성된 시간 기준
    updated_at = models.DateTimeField(auto_now=True)  # 해당 object 업데이트된 시간 기준

    class Meta:
        abstract = True  # 추상 클래스로 생성 (DB를 따로 만들지 않는다.)


class Category(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    name = models.CharField(max_length=255, unique=True)  # 카테고리 이름

    def __str__(self):
        return self.name


class Banner(CommonModel):
    id = models.BigAutoField(primary_key=True)  # Primary Key로 설정된 테이블 ID
    image = models.ImageField(upload_to="Banner_images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="banners")  # 카테고리 테이블 참조
    url_link = models.URLField()

    def __str__(self):
        return f"Banner {self.id}"
