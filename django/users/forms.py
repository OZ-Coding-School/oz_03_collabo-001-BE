from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser
class CustomAdminAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = CustomUser  # CustomUser 모델을 사용
        fields = ['email', 'password']
