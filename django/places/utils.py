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


def get_place_image_url():
    urls = [
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F60431621-d594-4e1b-a537-24c111bb155b%2Fimage.png?table=block&id=83403c34-b854-42de-b1f9-78169c53230a&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F24e1e56f-77b6-4b9f-afa7-3364e2143c7c%2Fimage.png?table=block&id=52da95fe-3f3d-4515-aaac-60ac909e1250&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=580&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F686099ba-5e04-445e-9c4e-c4ca6166906a%2Fimage.png?table=block&id=02cc5a1c-541b-4f8b-bcac-6fdbf2954a0d&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=450&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F1941192a-b8aa-4359-9d79-09acdd26fda5%2Fimage.png?table=block&id=bda8ab80-6e84-4410-83b4-88c27ebd8023&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fbf6c38f5-5445-4132-93d2-8e3b3588056e%2Fimage.png?table=block&id=37aab12b-aa82-4674-9ade-0b652eb2f61f&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
    ]
    return random.choice(urls)


def get_random_comment_for_recommend_place():
    comments = [
        "아늑한 분위기에서 아이와 반려견이 함께할 수 있는 카페",
        "놀이방이 있는 넓은 실내 공간에서 아이들과 함께 즐기세요",
        "반려견을 위한 전용 메뉴가 준비된 펫 프렌들리 카페",
        "아이와 반려견 모두가 행복한 시간을 보낼 수 있는 공간",
        "카페에서 아이와 반려견의 특별한 추억을 만들어 보세요",
        "친환경 장난감과 자연 친화적인 인테리어가 돋보이는 카페",
        "자연 속에서 아이와 반려견이 함께 뛰놀 수 있는 힐링 공간",
        "안전한 놀이 시설이 구비된 어린이 놀이터가 있는 카페",
        "아이를 위한 독서 공간과 반려견을 위한 놀이 공간이 함께 있는 곳",
        "반려견과 아이가 함께 즐길 수 있는 다양한 액티비티 제공",
        "도심 속에서 자연을 만끽할 수 있는 아이와 반려견을 위한 카페",
        "따뜻한 햇살 아래에서 즐기는 아이와 반려견을 위한 야외 테라스",
        "아이와 반려견을 위한 건강한 스낵 메뉴가 있는 카페",
        "아이와 반려견의 사진 촬영을 위한 포토존이 있는 카페",
        "조용하고 편안한 분위기에서 아이와 반려견이 함께할 수 있는 공간",
        "아이와 반려견을 위한 특별한 이벤트와 체험 프로그램 제공",
        "대형 놀이터와 반려견 전용 운동장이 있는 카페",
        "아이와 반려견이 함께 즐길 수 있는 놀이기구가 구비된 카페",
        "다양한 반려견 전용 용품이 준비된 카페",
        "아이와 반려견의 생일 파티를 위한 전용 공간이 있는 카페",
        "아이와 반려견이 함께 참여할 수 있는 요리 체험 프로그램 제공",
        "자연 속에서 아이와 반려견이 안전하게 뛰어놀 수 있는 카페",
        "아이와 반려견을 위한 그림책과 동화책이 준비된 공간",
        "놀이방과 반려견 전용 목욕 시설이 있는 카페",
        "아이와 반려견이 함께 힐링할 수 있는 마사지 서비스 제공",
        "신선한 주스와 반려견 전용 간식이 있는 건강 카페",
        "아이와 반려견이 함께 참여하는 핸드메이드 클래스 제공",
        "편안한 쇼파와 넓은 공간에서 아이와 반려견이 함께 휴식을 취할 수 있는 카페",
        "반려견을 위한 미니 운동회와 아이를 위한 체험학습 제공",
        "아이와 반려견이 함께하는 특별한 하루를 위한 카페",
    ]
    return random.choice(comments)


def get_random_place_store_image():
    random_images_url = [
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F0c1c6984-21a6-4cf6-97b9-bf84cae0addd%2Fimages.jpg?table=block&id=44f73b84-b184-4955-9a73-68410317e546&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Ff51589bc-73d4-4201-bf79-a51b2237603f%2Fimages.jpg?table=block&id=6b1f614c-32a9-428e-80ad-20a0c90e48f7&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Ff5b70156-f9fd-4ecf-9543-43dedb5d1cb1%2Fdownload.jpg?table=block&id=f1aef8ea-4440-45de-88bd-e1644e8c7fbe&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=450&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fc7cf17e5-f352-47b1-97c1-85f87c559950%2Fimages.jpg?table=block&id=5d980a29-baab-41c8-878b-18920cc39995&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F75895675-353b-481a-b576-2cd8ce091178%2Fdownload.jpg?table=block&id=af012d3a-fd5d-4d0d-98df-7991a0211180&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=580&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F12756335-af38-465b-aef7-83ee18f409ce%2Fimages.jpg?table=block&id=eb8bca1e-a532-4c45-9ad2-8f83c5bae7f5&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F531a9a03-7dd1-4d42-b4a1-409b9adf766b%2Fimages.jpg?table=block&id=5e1cd694-f75b-4cdd-8361-0927f0807a0f&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=580&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F7e86ff19-56e7-4d7b-b8b9-159ba4b5c824%2Fimages.jpg?table=block&id=1099742f-12fd-4ae1-92f0-90605e5f9435&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=390&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F4201c4e3-a838-4565-a039-823c63fb6554%2Fimages.jpg?table=block&id=ac09e2c3-8c76-4081-8718-099c3eccb902&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
    ]
    
    return random.choice(random_images_url)
