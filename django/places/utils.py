import random
import string


def generate_random_placename():
    words = [
        "펫프렌들리 카페",
        "멍멍이와 함께",
        "피치카페 애견동반",
        "도그프렌드 카페",
        "베이비앤도그 카페",
        "멍냥카페",
        "리틀 펫 가든",
        "하늘 정원 카페",
        "도그 스토리 카페",
        "애견카페 허그",
        "펫 카페 그린파크",
        "퍼피 러브 카페",
        "베이비 카페",
        "애견동반 레스토랑",
        "도그 카페 썬샤인",
        "베이비펫 카페",
        "펫과 함께하는 공간",
        "도그 프렌드 레스토랑",
        "피크닉 카페",
        "베이비 멍멍 카페",
        "펫 프렌들리 존",
        "애견동반 레스토랑",
        "도그 힐링 카페",
        "펫 카페 루나",
        "멍냥이 카페",
        "도그 앤 키즈 카페",
        "펫 카페 해피",
        "애견동반 카페 몽이",
        "아이와 펫 카페",
        "도그 헬스 카페",
        "베이비 펫 플레이스",
        "펫동반 카페 힐링",
        "멍멍이와 베이비",
        "도그 카페 포레스트",
        "펫 카페 파라다이스",
        "아이와 펫 카페",
        "펫프렌들리 카페",
        "애견 카페 허그",
        "도그 파크 카페",
        "베이비와 펫 카페",
        "펫동반 카페 피크닉",
        "도그프렌들리 카페",
        "멍멍이와 함께하는 카페",
        "아이와 펫의 공간",
        "베이비펫 카페",
        "도그 힐링 존",
        "펫 카페 베리",
        "애견동반 카페 스토리",
        "도그 앤 키즈 레스토랑",
        "펫 프렌들리 카페",
        "도그 프렌드 파크",
        "애견동반 카페 로즈",
        "펫과 아이의 쉼터",
        "멍멍이 플레이 카페",
        "베이비 도그 카페",
        "펫 프렌들리 하우스",
        "도그 카페 스카이",
        "애견동반 카페 노을",
        "펫 & 베이비 카페",
        "도그 러버 카페",
        "베이비펫 힐링 존",
        "펫동반 카페 미소",
        "멍멍이와 아이의 놀이터",
        "도그 키즈 카페",
        "펫 카페 블루문",
        "애견동반 레스토랑 리프",
        "도그 프렌드 존",
        "펫과 함께하는 카페",
        "아이와 도그 카페",
        "베이비펫 플레이 카페",
        "도그 카페 라이트",
        "펫동반 카페 마이펫",
        "멍멍이와 함께 카페",
        "애견동반 레스토랑 그린",
        "펫 카페 웰컴",
        "도그 앤 베이비 카페",
        "펫프렌들리 카페 해피",
        "애견동반 카페 플레이",
        "도그 카페 해피네스",
        "베이비펫 카페 선샤인",
        "펫과 아이의 카페",
        "멍냥이와 함께하는 카페",
        "도그 힐링 레스토랑",
        "펫 카페 마이펫",
        "애견동반 카페 해피데이",
        "도그 앤 베이비 플레이스",
        "펫프렌들리 카페 오아시스",
        "애견동반 카페 클로버",
        "도그 카페 퍼피존",
        "베이비와 펫의 카페",
        "펫동반 카페 스마일",
        "멍멍이와 노는 카페",
        "애견동반 레스토랑 블루",
        "펫 카페 그린필드",
        "도그 앤 키즈 존",
        "펫프렌들리 카페 스토리",
        "애견동반 카페 프렌즈",
        "도그 러버 레스토랑",
        "베이비펫 플레이존",
        "펫동반 카페 오션",
    ]
    word = random.choice(words)
    suffix = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    return f"{word}{suffix}"


def generate_random_ServiceIcon(n):
    n = int(n)
    if int(n) >= 7:
        raise ValueError("The number of service icons must be less than or equal to 6.")

    words = [
        "~5kg",
        "소형견",
        "애견동반",
        "무선인터넷",
        "주차가능",
        "바베큐장",
        "드라이브 스루",
    ]

    image_urls = [
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F902b5c77-e2a7-4ed1-ab92-f5eb8ff3327f%2Fkettlebell_6865501.png?table=block&id=a3c39552-c64f-40bb-be10-71b35ca3680e&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fc97c52e2-6e57-49a1-9ad3-699fa5b814fe%2Fdog_1650609.png?table=block&id=e38d7ad2-04d9-4bd4-bf3a-d1c5cdcfc7b7&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F82f91650-a1b9-446b-8c8b-6d38db7575bf%2Fshopping-basket_886669.png?table=block&id=addcf09d-d0e6-4b27-a7a8-2be77f1f4231&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fcb564da6-6251-4255-a25b-50bedc0084ff%2Fwifi_2859724.png?table=block&id=73752ad7-129a-4238-9334-96f8ae4f63db&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fced19847-81b6-4e66-9ad4-0b46f75be4a9%2Fparking_751330.png?table=block&id=02856686-742b-43f0-8cef-90ec0de6a6d4&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F1c65fe41-fe8f-4d86-87fe-ed89933902c0%2Fmeat_1406853.png?table=block&id=53b38845-d5ed-4c1c-bec7-abe36b052db1&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F6814ebba-f230-4c6b-b7d3-e7f859baf340%2Fdrive_6008006.png?table=block&id=bf599779-37ea-404c-af47-b514f472cd9c&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=1020&userId=&cache=v2",
    ]
    return [words[n], image_urls[n]]


import urllib.request

from django.core.files.temp import NamedTemporaryFile


def get_image_by_url(url):
    try:
        # 사용자 에이전트를 설정하여 요청
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        request = urllib.request.Request(url, headers=headers)

        img_temp = NamedTemporaryFile()  # 임시 파일 생성
        img_temp.write(urllib.request.urlopen(request).read())  # URL에서 이미지 데이터를 읽어 임시 파일에 저장
        img_temp.flush()  # 파일에 기록된 내용을 디스크에 반영
        return img_temp  # 임시 파일을 반환 (닫지 않고 반환)
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        return None
