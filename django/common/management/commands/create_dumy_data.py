import os
import urllib.request

from common.models import Banner, Category
from places.models import ServicesIcon
from users.utils import generate_random_nickname

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create initial data for Category and Banner models"

    def handle(self, *args, **kwargs):
        categories = [
            "마이페이지",
            "애개플레이스",
            "펫존",
            "키즈존",
        ]

        image_url = "https://avatars.githubusercontent.com/u/21354840?v=4"

        try:

            img_temp = NamedTemporaryFile()
            img_temp.write(urllib.request.urlopen(image_url).read())
            img_temp.flush()

            for category_name in categories:
                category = Category.objects.get(name=category_name)
                self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created successfully.'))

                for i in range(10):
                    # Download the image

                    # Create Banner instance
                    banner = Banner(
                        category=category,
                        url_link=f"https://example.com/{category_name}/{i}",
                        visible=True,
                    )
                    banner.image.save(f"{category_name}_{i}.jpg", File(img_temp))
                    banner.save()

                    self.stdout.write(self.style.SUCCESS(f'Banner "{category_name}_{i}" created successfully.'))

            for i in range(10):
                servicesicon = ServicesIcon(
                    name=generate_random_nickname(),
                )
                servicesicon.image.save(f"{category_name}_{i}.jpg", File(img_temp))
                servicesicon.save()

                self.stdout.write(self.style.SUCCESS(f'servicesicon "{servicesicon}" created successfully.'))

            self.stdout.write(self.style.SUCCESS("Dumy data creation completed successfully."))

        except Exception as e:
            print(e)
        finally:
            # Close and delete the temporary file
            img_temp.close()
