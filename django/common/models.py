from django.db import models

# 공통 사용 모델클레스
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 해당 object 생성된 시간 기준
    updated_at = models.DateTimeField(auto_now=True) # 해당 object 업데이트된 시간 기준

    class Meta:
        abstract = True # 추상 클래스로 생성 (DB를 따로 만들지 않는다.)