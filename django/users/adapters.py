# yourapp/adapters.py
# 소셜 로그인 프로필 데이터 동기화
# 소셜 로그인시 소셜에서 데이터 가져오기
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        user.email = data.get('email')
        user.nickname = data.get('nickname')
        user.profile_image = sociallogin.account.extra_data.get('profile_image', None)
        return user
