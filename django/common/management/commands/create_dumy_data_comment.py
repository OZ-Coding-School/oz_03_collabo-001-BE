import random

from places.models import CommentImage, Comments, Place
from places.utils import get_random_comment_content  # 랜덤 댓글 내용을 가져오는 함수
from places.utils import get_image_by_url, get_random_place_store_image
from users.models import CustomUser

from django.core.files import File
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create random comments for Places from a range of users"

    def add_arguments(self, parser):
        # Command-line arguments for specifying user ID range
        parser.add_argument("start_id", type=int, help="Start ID for user range")
        parser.add_argument("end_id", type=int, help="End ID for user range")

    def handle(self, *args, **kwargs):
        # Retrieve the start and end ID from command-line arguments
        start_id = kwargs["start_id"]
        end_id = kwargs["end_id"]

        try:
            # 지정된 범위의 유저 가져오기
            users = list(CustomUser.objects.filter(id__gte=start_id, id__lte=end_id))  # 범위 지정

            if not users:
                self.stdout.write(self.style.ERROR(f"No users found between ID {start_id} and {end_id}."))
                return

            # 전체 Place 가져오기
            places = Place.objects.all()

            for place in places:
                # 각 Place에 대해 지정된 유저가 랜덤으로 1~5개의 댓글 작성
                for _ in range(random.randint(1, 5)):  # 1~5개의 댓글 생성
                    user = random.choice(users)  # 유저를 랜덤으로 선택
                    comment = Comments(
                        user=user,
                        place=place,
                        content=get_random_comment_content(),  # 랜덤 댓글 내용
                        rating=random.randint(1, 5),  # 1~5점 사이의 별점 랜덤 선택
                    )
                    comment.save()

                    # 랜덤으로 1~5개의 이미지 추가
                    for _ in range(random.randint(1, 5)):
                        comment_image = CommentImage(
                            comment=comment,
                        )
                        comment_image.image.save(
                            f"comment_{comment.id}_image_{random.randint(1, 100)}.jpg",
                            File(get_image_by_url(get_random_place_store_image())),  # 랜덤 이미지 URL로 이미지 추가
                        )
                        comment_image.save()

                    self.stdout.write(
                        self.style.SUCCESS(f'Comment by "{user.nickname}" for "{place.name}" created successfully.')
                    )

            self.stdout.write(self.style.SUCCESS("Comments and images have been added for each place."))

        except Exception as e:
            print(f"Error: {e}")
