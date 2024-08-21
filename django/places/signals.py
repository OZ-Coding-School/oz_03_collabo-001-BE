import math

from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comments


@receiver(post_save, sender=Comments)
def update_place_rating(sender, instance, created, **kwargs):
    place = instance.place

    # 댓글의 평균 rating 계산
    avg_rating = place.comments.aggregate(Avg("rating"))["rating__avg"]

    if avg_rating is not None:
        # 소수점 3째자리에서 반올림하여 rating_float에 저장
        place.rating_float = round(avg_rating, 3)
        # 소수점 1째자리에서 반올림하여 rating에 저장
        place.rating = round(avg_rating)

        place.save()
