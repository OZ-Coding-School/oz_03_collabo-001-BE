import random
import time

from common.models import Banner, Category
from geopy.geocoders import Nominatim
from places.models import (
    CommentImage,
    Comments,
    Place,
    PlaceDescriptionImage,
    PlaceImage,
    PlaceRegion,
    PlaceSubcategory,
    RecommendCategory,
    RecommendedPlace,
    RecommendTags,
    ServicesIcon,
)
from places.utils import (
    generate_random_placename,
    generate_random_ServiceIcon,
    get_image_by_url,
    get_place_image_url,
    get_random_comment_for_recommend_place,
)
from users.models import BookMark, CustomUser, ViewHistory

from django.core.files import File
from django.core.management.base import BaseCommand


def getRandomAddress():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        min_lat, max_lat = 35.136077, 37.680704
        min_lon, max_lon = 126.659877, 128.945123
        random_latitude = random.uniform(min_lat, max_lat)
        random_longitude = random.uniform(min_lon, max_lon)
        time.sleep(0.5)
        location = geolocator.reverse((random_latitude, random_longitude), exactly_one=True, language="ko")

        if location:
            random_address = " ".join(location.address.split(",")[::-1]).strip()
        else:
            random_address = "some address"
        return random_address
    except:
        return "some address"


class Command(BaseCommand):
    help = "Create initial data for Category, Banner, Place, and Comments models"

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
                    if category_name == "마이페이지" and i != 0:
                        continue

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

            services_icons = list(ServicesIcon.objects.all())
            place_regions = list(PlaceRegion.objects.all())
            place_subcategories = list(PlaceSubcategory.objects.all())

            if not services_icons or not place_regions or not place_subcategories:
                self.stdout.write(self.style.ERROR("필요한 외래 키 데이터가 부족합니다. 데이터베이스를 확인하세요."))
                return

            users = list(CustomUser.objects.filter(email__in=[f"{i}@admin.com" for i in range(1, 11)]))

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
                    user=random.choice(users),
                )

                place.store_image.save(f"place_store_image_{i}.jpg", File(get_image_by_url(image_url)))

                selected_icons = random.sample(services_icons, k=random.randint(1, min(2, len(services_icons))))
                place.service_icons.set(selected_icons)

                selected_region = random.choice(place_regions)
                place.place_region = selected_region

                selected_subcategory = random.choice(place_subcategories)
                place.place_subcategory = selected_subcategory

                for j in range(random.randint(3, 10)):
                    place_image = PlaceImage(
                        place=place,
                    )
                    place_image.image.save(f"place_{i+1}_image_{j+1}.jpg", File(get_image_by_url(image_url)))
                    place_image.save()

                for j in range(random.randint(3, 10)):
                    place_image = PlaceDescriptionImage(
                        place=place,
                    )
                    place_image.image.save(f"place_{i+1}_image_{j+1}.jpg", File(get_image_by_url(image_url)))
                    place_image.save()

                place.save()
                self.stdout.write(self.style.SUCCESS(f'Place "{place.name}" created successfully.'))

                # Create comments for the place
                for _ in range(random.randint(3, 6)):
                    user = random.choice(users)
                    comment = Comments(
                        user=user,
                        place=place,
                        content=f"Some content for {place.name} with {user.nickname}",
                        rating=random.choice([1, 2, 3, 4, 5]),
                    )
                    comment.save()

                    # Add random images to the comment
                    for _ in range(random.randint(1, 5)):
                        comment_image = CommentImage(
                            comment=comment,
                        )
                        comment_image.image.save(
                            f"comment_{comment.id}_image_{random.randint(1, 100)}.jpg",
                            File(get_image_by_url(get_place_image_url())),
                        )
                        comment_image.save()

                    self.stdout.write(
                        self.style.SUCCESS(f'Comment by "{user.nickname}" for "{place.name}" created successfully.')
                    )

            users = CustomUser.objects.all()
            places = list(Place.objects.all())

            if not places:
                self.stdout.write(self.style.ERROR("No places found in the database."))
                return

            for user in users:
                # Bookmarks
                random_places_for_bookmarks = random.sample(places, min(10, len(places)))
                for place in random_places_for_bookmarks:
                    bookmark, created = BookMark.objects.get_or_create(user=user, place=place)
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Bookmark created for {user.nickname} - {place.name}"))

                # View Histories
                random_places_for_viewhistories = random.sample(places, min(10, len(places)))
                for place in random_places_for_viewhistories:
                    view_history, created = ViewHistory.objects.get_or_create(user=user, place=place)
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"ViewHistory created for {user.nickname} - {place.name}"))

            self.stdout.write(self.style.SUCCESS("Bookmarks and ViewHistories have been added for each user."))

            places = list(Place.objects.all())
            tags = list(RecommendTags.objects.all())
            categories = RecommendCategory.objects.all()

            if not places or not tags or not categories:
                self.stdout.write(self.style.ERROR("필요한 외래 키 데이터가 부족합니다. 데이터베이스를 확인하세요."))
                return

            for category in categories:
                num_places = random.randint(3, 6)  # 3에서 6개의 RecommendedPlace 생성
                for _ in range(num_places):
                    selected_place = random.choice(places)  # 랜덤한 Place 선택
                    selected_tags = random.sample(tags, random.randint(3, 6))  # 3에서 6개의 랜덤한 Tags 선택

                    recommended_place = RecommendedPlace.objects.create(
                        place=selected_place, category=category, content=get_random_comment_for_recommend_place()
                    )
                    recommended_place.tags.set(selected_tags)
                    recommended_place.save()

                    self.stdout.write(
                        self.style.SUCCESS(
                            f'RecommendedPlace "{recommended_place.place.name}" created successfully with tags: {", ".join(tag.tag for tag in selected_tags)}'
                        )
                    )

            self.stdout.write(self.style.SUCCESS("All RecommendedPlaces created successfully."))

            self.stdout.write(self.style.SUCCESS("Dummy data creation completed successfully."))

        except Exception as e:
            print(e)
