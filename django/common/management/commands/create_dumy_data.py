import os
import random
import time
import urllib.request

from common.models import Banner, Category
from geopy.geocoders import Nominatim
from places.models import Place, PlaceImage, PlaceRegion, PlaceSubcategory, ServicesIcon
from places.utils import (
    generate_random_placename,
    generate_random_ServiceIcon,
    get_image_by_url,
)
from users.models import CustomUser
from users.utils import generate_random_nickname

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand


def getRandomAddress():
    try:
        # Nominatim 지오코더 객체 생성
        geolocator = Nominatim(user_agent="geoapiExercises")

        # 위도와 경도의 범위 설정 (한국 대부분 지역)
        min_lat, max_lat = 35.136077, 37.680704
        min_lon, max_lon = 126.659877, 128.945123

        # 랜덤한 위도와 경도 생성
        random_latitude = random.uniform(min_lat, max_lat)
        random_longitude = random.uniform(min_lon, max_lon)

        time.sleep(0.5)

        # 랜덤 좌표로부터 주소 얻기
        location = geolocator.reverse((random_latitude, random_longitude), exactly_one=True, language="ko")

        if location:
            random_address = " ".join(location.address.split(",")[::-1]).strip()
        else:
            random_address = "some address"
        return random_address
    except:
        return "some address"


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
                    banner.image.save(f"{category_name}_{i}.jpg", File(get_image_by_url(image_url)))
                    banner.save()

                    self.stdout.write(self.style.SUCCESS(f'Banner "{category_name}_{i}" created successfully.'))

            for i in range(7):
                serviceIconName, ServiceIconImageUrl = generate_random_ServiceIcon(i)
                servicesicon = ServicesIcon(
                    name=serviceIconName,
                )
                servicesicon.image.save(f"servicesicon_{i}.jpg", File(get_image_by_url(ServiceIconImageUrl)))
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
            for i in range(30):

                place = Place(
                    name=generate_random_placename(),
                    description_tags=f"Description for place {i+1}",
                    address=getRandomAddress(),
                    price_text=f"10000{i+1}",
                    price_link="https://example.com",
                    rating=random.choice([1, 2, 3, 4, 5]),
                    instruction=f"Some instructions {i+1}",
                    category=random.choice(["bd_zone", "kid_zone", "pet_zone"]),
                    user=CustomUser.objects.first(),  # Assuming there is at least one user
                )

                place.store_image.save(f"place_store_image_{i}.jpg", File(get_image_by_url(image_url)))

                # Assign a random number of service icons (1 to 10)
                selected_icons = random.sample(services_icons, k=random.randint(1, min(2, len(services_icons))))
                place.service_icons.set(selected_icons)

                # Place Region - 1 random selection
                selected_region = random.choice(place_regions)

                place.place_region = selected_region

                # Place Subcategory - 1 random selection
                selected_subcategory = random.choice(place_subcategories)
                place.place_subcategory = selected_subcategory

                for j in range(10):
                    place_image = PlaceImage(
                        place=place,
                    )
                    place_image.image.save(
                        f"place_{i+1}_image_{j+1}.jpg", File(get_image_by_url(image_url))
                    )  # Save the image to the temporary file
                    place_image.save()

                place.save()
                self.stdout.write(self.style.SUCCESS(f'Place "{place.name}" created successfully.'))

            self.stdout.write(self.style.SUCCESS("Dumy data creation completed successfully."))

        except Exception as e:
            print(e)
