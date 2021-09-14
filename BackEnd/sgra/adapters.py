from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from profileapp.models import Profile


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        social_app_name = sociallogin.account.provider.upper()

        # profile create
        if social_app_name == 'KAKAO':
            thumbnail = sociallogin.account.extra_data['kakao_account']['profile']['thumbnail_image_url']
        elif social_app_name == 'GOOGLE':
            thumbnail = sociallogin.account.extra_data['picture']
        elif social_app_name == 'NAVER':
            thumbnail = sociallogin.account.extra_data['profile_image']

        Profile(user=user, nickname=user.username, thumbnail=thumbnail).save()
