from common.models import Category

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create initial data for Category model"

    def handle(self, *args, **kwargs):
        # Check if the Category model is empty
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING("데이터가 있습니다."))
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
