from common.models import Category
from places.models import PlaceRegion, PlaceSubcategory, RecommendCategory

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create initial data for Category model"

    def handle(self, *args, **kwargs):
        # Check if the Category model is empty
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING("Category 데이터가 있습니다."))
        else:
            categories = [
                "마이페이지",
                "애개플레이스",
                "펫존",
                "키즈존",
            ]

            for name in categories:
                Category.objects.create(name=name)
                self.stdout.write(self.style.SUCCESS(f'Category "{name}" created successfully.'))

        if RecommendCategory.objects.exists():
            self.stdout.write(self.style.WARNING("RecommendCategory 데이터가 있습니다."))
        else:
            categories = [
                "애개플레이스",
                "펫존",
                "키즈존",
            ]

            for name in categories:
                RecommendCategory.objects.create(name=name)
                self.stdout.write(self.style.SUCCESS(f'RecommendCategory "{name}" created successfully.'))

        if PlaceRegion.objects.exists():
            self.stdout.write(self.style.WARNING("PlaceRegion 데이터가 있습니다."))
        else:
            categories = [
                "서울",
                "경기",
                "인천",
                "충청",
                "강원",
                "전라",
                "경상",
                "제주",
            ]

            for region in categories:
                PlaceRegion.objects.create(region=region)
                self.stdout.write(self.style.SUCCESS(f'PlaceRegion "{region}" created successfully.'))

        if PlaceSubcategory.objects.exists():
            self.stdout.write(self.style.WARNING("PlaceSubcategory 데이터가 있습니다."))
        else:
            categories = [
                "카페",
                "펜션",
                "음식점",
                "야외/공원",
            ]

            for subcategory in categories:
                PlaceSubcategory.objects.create(subcategory=subcategory)
                self.stdout.write(self.style.SUCCESS(f'Category "{subcategory}" created successfully.'))
