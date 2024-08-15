import os
import urllib.request
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from common.models import Category, Banner

class Command(BaseCommand):
    help = 'Create initial data for Category and Banner models'

    def handle(self, *args, **kwargs):
        # Check if the Category model is empty
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('데이터가 있습니다.'))
            return

        categories = [
            "마이페이지",
            "애개플레이스",
            "펫존",
            "키즈존",
        ]

        image_url = "https://avatars.githubusercontent.com/u/21354840?v=4"

        for category_name in categories:
            category = Category.objects.create(name=category_name)
            self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created successfully.'))

            for i in range(10):
                # Download the image
                img_temp = NamedTemporaryFile()
                img_temp.write(urllib.request.urlopen(image_url).read())
                img_temp.flush()

                # Create Banner instance
                banner = Banner(
                    category=category,
                    url_link=f"https://example.com/{category_name}/{i}",
                    visible=True,
                )
                banner.image.save(f"{category_name}_{i}.jpg", File(img_temp))
                banner.save()

                self.stdout.write(self.style.SUCCESS(f'Banner "{category_name}_{i}" created successfully.'))

                # Close and delete the temporary file
                img_temp.close()

        self.stdout.write(self.style.SUCCESS('Initial data creation completed successfully.'))
