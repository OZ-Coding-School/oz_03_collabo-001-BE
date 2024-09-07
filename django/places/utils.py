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
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F07fcf199-55d0-410c-af5d-6e755aed096a%2Fimage.png?table=block&id=95db02f6-258f-4487-8a09-1d14d769086d&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F9218193e-d955-4274-b264-544ddcb7be0c%2Fimage.png?table=block&id=36ffba65-541b-4a97-893b-aec5a5c7dab5&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fb9d6a8fb-6d96-4a13-b71e-d0eadec3bfc8%2Fimage.png?table=block&id=db23ca1b-3a61-4dce-9390-08eba5d7ad99&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F74ddb093-bdea-4f45-b85f-d3c415cff172%2Fimage.png?table=block&id=e4b967be-f6bb-446d-a11e-49d6e22b5ecf&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fa1da3270-450e-4f08-87ab-5ee009a1fad0%2Fimage.png?table=block&id=95d2ccb6-d2e6-49db-a9e5-6f2a809c0af5&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F75b15cc2-e88b-4572-a8e0-910f48235e12%2Fimage.png?table=block&id=4e12d555-444d-4046-8c6a-bbce3ef255b8&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F6b628696-bf74-41ad-876b-db53f77d1b92%2Fimage.png?table=block&id=fca4e949-4517-41a7-8089-ea751c70e07b&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F0a1d751a-41cc-46b0-b478-793f0331aa78%2Fimage.png?table=block&id=14fe27c9-f010-4516-a0c5-0cfc36f35c5a&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F255a3f47-59da-4fc1-a9b3-9612287e1cd3%2Fimage.png?table=block&id=3d6e5581-c528-403e-9db5-9dfdff415324&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fb4c8e6f0-33fe-4a30-bf0f-a4243088a0ef%2Fimage.png?table=block&id=d60f01ab-014f-49c2-a44e-eebcb7328ae8&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=400&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F748d0e14-2b98-4047-9f94-e8c443e76c34%2Fimage.png?table=block&id=814cdaa9-83d7-4805-a35c-4469eaffb878&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=610&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F4c4575d8-6f87-49f4-a90b-648949fe202e%2Fimage.png?table=block&id=f64b15c9-e816-4ee7-94fb-9cc758c6d87e&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=600&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F8770681f-806c-48d7-a655-c1f78af6c665%2Fimage.png?table=block&id=905cb93f-ba58-427b-8057-81be0728a8e6&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F5f69f6a4-acf4-4c12-bc5b-74b25ac4fb69%2Fimage.png?table=block&id=a8063d25-44f1-4e08-a2d2-bcdaafc2f228&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=610&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F9bc41c10-3f43-4ea0-b2e3-e7d192b10da8%2Fimage.png?table=block&id=895dd5a4-e241-4963-975f-3d867250747e&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F50b4449e-8247-4c52-9d3c-2cf09a4a2871%2Fimage.png?table=block&id=e3429228-4f32-498e-a2ce-ab9fa10e8baf&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=540&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fbef8e3d8-3bfb-4298-9f2d-e836165cb6f2%2Fimage.png?table=block&id=659284c0-05fe-4ff8-9149-3d502fe72e14&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=520&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Fab1c7079-801e-4805-9cf8-b618c792bc4c%2Fimage.png?table=block&id=fd93c41e-6c5c-4996-9a27-e706c2684b4d&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2F2e95cd04-1cb3-4926-bf98-cfeddf48a107%2Fimage.png?table=block&id=a5e75c24-0c9f-41b2-a600-4050653ee61f&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=570&userId=&cache=v2",
        "https://longing-paperback-1b8.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F8a3de105-c56b-42f5-bf1e-24a149af8068%2Ffcfb601f-247e-4587-92a8-961194688dcd%2Fimage.png?table=block&id=3c0ec053-7484-4456-812d-5f687cececaa&spaceId=8a3de105-c56b-42f5-bf1e-24a149af8068&width=550&userId=&cache=v2",
    ]

    return random.choice(random_images_url)


def get_random_comment_content():

    comments = [
        "이곳은 저희 강아지도 너무 좋아했어요! 깨끗하고 안전한 공간이라 안심하고 놀았답니다.",
        "아이와 함께 방문했는데, 너무 즐거운 시간을 보냈어요. 추천합니다!",
        "반려견을 위한 배려가 가득한 곳이에요. 정말 마음에 듭니다!",
        "넓은 공간에서 강아지가 마음껏 뛰어놀 수 있었어요. 최고의 장소!",
        "아이와 강아지가 함께 즐길 수 있는 완벽한 장소에요!",
        "여기 서비스 정말 친절해요! 다시 오고 싶어요!",
        "반려견도 너무 편안해 보였고, 가족 모두가 즐거운 시간을 보냈어요.",
        "아이와 함께할 수 있는 장소를 찾고 있었는데, 딱이에요!",
        "너무 사랑스러운 공간이에요. 강아지가 정말 행복해 했답니다.",
        "친절한 직원분들 덕분에 더욱 편하게 이용할 수 있었어요.",
        "아이도 강아지도 모두 만족한 시간! 꼭 다시 방문할 거예요.",
        "강아지와 산책하기 좋은 공간이 많아서 정말 좋았어요.",
        "이런 곳이 더 많았으면 좋겠어요! 최고의 장소입니다.",
        "아이와 강아지가 모두 즐거워하는 모습에 저도 기분이 좋아졌어요!",
        "깔끔하고 정돈된 공간이라 반려동물과 아이 모두 안심하고 놀 수 있어요.",
        "강아지 간식도 준비되어 있어서 너무 좋았어요!",
        "반려견도 환영받는 공간이라 자주 올 것 같아요.",
        "아이들과 강아지를 위한 최적의 공간이에요!",
        "서비스와 시설 모두 최고! 꼭 와보세요.",
        "강아지가 정말 좋아했어요. 마음이 편해지는 장소입니다.",
        "아이와 강아지 모두 신나게 뛰어놀 수 있는 완벽한 공간!",
        "너무 아늑하고 사랑스러운 분위기였어요.",
        "강아지가 좋아하는 놀이터 같은 곳이에요. 아이도 신났답니다.",
        "반려동물을 위한 세심한 배려가 돋보이는 곳입니다.",
        "가족과 함께 즐거운 시간 보냈어요. 추천합니다!",
        "아이도 강아지도 너무 행복해 했어요. 다시 방문할 거예요.",
        "직원들이 정말 친절해서 감동했어요!",
        "강아지를 위한 공간이 너무 잘 되어 있어요.",
        "여기 분위기가 너무 좋아요. 강아지와 함께라 더 행복했어요!",
        "아이와 함께 산책하기 너무 좋은 공간이에요.",
        "강아지와 아이 모두를 위한 천국 같은 곳!",
        "강아지 놀이터가 너무 잘 되어 있어서 자주 올 것 같아요.",
        "아이와 강아지가 모두 좋아하는 완벽한 장소!",
        "친절한 서비스와 깨끗한 환경이 최고였어요.",
        "아이와 강아지가 함께 놀기 좋은 안전한 공간이에요.",
        "아이와 함께할 수 있는 반려견 공간을 찾았는데, 여기 너무 좋았어요.",
        "강아지가 너무 즐거워해서 보는 내내 기분이 좋았어요.",
        "아이와 강아지가 행복해할 수 있는 완벽한 장소에요.",
        "공간이 넓어서 강아지가 자유롭게 뛰어놀 수 있었어요.",
        "아이와 함께 방문했는데, 너무 편안하고 즐거웠어요.",
        "강아지가 마음껏 놀 수 있는 곳이라 정말 좋았어요!",
        "여기 와서 강아지와 아이가 정말 신나했어요!",
        "깨끗하고 사랑스러운 장소라서 자주 올 것 같아요.",
        "아이와 강아지 모두를 배려한 공간이에요. 정말 좋습니다!",
        "친절한 서비스 덕분에 더욱 즐거운 시간을 보냈어요.",
        "아이와 강아지가 함께 행복해할 수 있는 공간이었어요.",
        "강아지가 너무 좋아해서 또 올 거예요!",
        "아이도 강아지도 모두 신나게 놀 수 있는 곳이라 좋았어요.",
        "강아지를 위한 공간이 너무 잘 되어 있어요. 추천합니다!",
        "아이와 함께하기에 딱 좋은 장소였어요!",
        "강아지도 아이도 정말 즐거워해서 너무 행복했어요.",
        "강아지와 함께할 수 있는 완벽한 공간이에요.",
        "아이와 반려견 모두를 위한 공간이어서 너무 좋았어요.",
        "시설도 좋고 직원분들도 친절해서 마음에 쏙 들었어요.",
        "아이와 강아지 모두가 행복해했던 시간! 감사합니다!",
        "이곳은 정말 강아지와 아이가 함께하기에 최적의 장소에요.",
        "편안한 분위기 덕분에 아이도 강아지도 모두 좋아했어요.",
        "강아지가 마음껏 뛰어놀 수 있어서 정말 좋았어요.",
        "아이와 강아지가 함께 놀기 좋은 공간이에요.",
        "강아지와 아이 모두 즐거워서 기분 좋은 하루를 보냈습니다.",
        "너무 아늑하고 편안한 공간이라 자주 올 것 같아요.",
        "아이와 강아지가 모두 만족한 시간이었어요!",
        "친절한 서비스와 편안한 공간, 정말 완벽한 곳이에요.",
        "아이와 강아지가 함께 놀기에 최적의 공간이에요.",
        "강아지를 위한 시설이 너무 잘 되어 있어서 다시 방문할 거예요.",
        "아이도 강아지도 정말 행복해 했어요. 최고의 장소입니다!",
        "이곳은 정말 아이와 강아지가 함께할 수 있는 최고의 공간이에요.",
        "아이와 강아지가 함께 즐길 수 있는 시설이 너무 잘 되어 있어요.",
        "강아지가 너무 행복해해서 자주 올 것 같아요.",
        "아이와 함께하는 시간을 더 행복하게 만들어준 장소에요.",
        "강아지를 위한 배려가 돋보이는 공간이에요.",
        "아이와 함께할 수 있어서 더 행복한 시간을 보냈어요.",
        "강아지가 정말 좋아하는 곳이에요. 다음에 또 올게요!",
        "아이와 강아지가 함께할 수 있어서 정말 좋은 시간이었어요.",
        "강아지가 신나서 놀았던 시간이었어요. 너무 좋습니다!",
        "아이와 강아지가 함께 즐길 수 있는 완벽한 공간이에요.",
        "시설이 너무 잘 되어 있어서 강아지도 아이도 행복해했어요.",
        "아이와 강아지 모두가 만족한 공간! 꼭 다시 오고 싶어요.",
        "강아지를 위한 공간이 잘 되어 있어서 자주 방문할 것 같아요.",
        "아이와 강아지가 모두 신나는 시간을 보냈어요. 정말 추천해요!",
        "여기 너무 사랑스러운 공간이에요. 강아지도 너무 좋아했어요.",
        "강아지가 너무 신나서 행복한 시간을 보냈어요!",
        "아이와 함께 방문했는데 너무 좋은 시간이었어요!",
        "강아지를 위한 배려가 가득한 공간이라 마음에 들어요.",
        "아이와 강아지가 모두 즐거워하는 모습이 너무 사랑스러웠어요.",
        "강아지와 함께할 수 있는 최고의 공간이에요.",
        "아이와 함께 방문하기에 딱 좋은 공간이에요.",
        "강아지를 위한 놀이터가 너무 잘 되어 있어요!",
        "아이와 강아지가 함께 즐길 수 있는 공간이어서 좋았어요.",
        "강아지가 너무 좋아해서 자주 방문할 것 같아요.",
        "아이와 강아지 모두를 위한 완벽한 공간이에요!",
        "강아지를 위한 배려가 가득한 곳이라 마음에 쏙 들었어요.",
    ]

    return random.choice(comments)
