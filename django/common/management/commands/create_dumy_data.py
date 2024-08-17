import os
import random
import urllib.request

from common.models import Banner, Category
from places.models import Place, PlaceImage, PlaceRegion, PlaceSubcategory, ServicesIcon
from users.models import CustomUser
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
                    # 마이페이지 더미데이터 1개만 생성
                    if category_name == "마이페이지" and i != 0:
                        continue

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
                servicesicon.image.save(f"servicesicon_{i}.jpg", File(img_temp))
                servicesicon.save()

                self.stdout.write(self.style.SUCCESS(f'servicesicon "{servicesicon}" created successfully.'))

            # Service Icons, Place Regions, Place Subcategories
            services_icons = list(ServicesIcon.objects.all())
            place_regions = list(PlaceRegion.objects.all())
            place_subcategories = list(PlaceSubcategory.objects.all())

            if not services_icons or not place_regions or not place_subcategories:
                self.stdout.write(self.style.ERROR("필요한 외래 키 데이터가 부족합니다. 데이터베이스를 확인하세요."))
                return

            # Place 더미데이터
            for i in range(10):
                place = Place(
                    name=generate_random_nickname(),
                    description=f"Description for place {i+1}",
                    address=f"Address for place {i+1}",
                    price_text="10000",
                    price_link="https://example.com",
                    rating=random.choice([1, 2, 3, 4, 5]),
                    instruction="Some instructions",
                    category=random.choice(["펫존", "키즈존"]),
                    user=CustomUser.objects.first(),  # Assuming there is at least one user
                )

                place.store_image.save(f"place_store_image_{i}.jpg", File(img_temp))

                # Assign a random number of service icons (1 to 10)
                selected_icons = random.sample(services_icons, k=random.randint(1, min(10, len(services_icons))))
                place.service_icons.set(selected_icons)

                # Place Region - 1 random selection
                selected_region = random.choice(place_regions)
                place.place_region.set([selected_region])

                # Place Subcategory - 1 random selection
                selected_subcategory = random.choice(place_subcategories)
                place.place_subcategory.set([selected_subcategory])

                for j in range(10):
                    place_image = PlaceImage(
                        place=place,
                    )
                    place_image.image.save(
                        f"place_{i+1}_image_{j+1}.jpg", File(img_temp)
                    )  # Save the image to the temporary file
                    place_image.save()

                place.save()
                self.stdout.write(self.style.SUCCESS(f'Place "{place.name}" created successfully.'))

            self.stdout.write(self.style.SUCCESS("Dumy data creation completed successfully."))

        except Exception as e:
            print(e)
        finally:
            # Close and delete the temporary file
            img_temp.close()
