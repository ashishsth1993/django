from django import forms
from .models import LandingPage


class LandingForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = [
            'brand_name',
            'brand_name_2',
            'brand_paragraph',
            'facebook_link',
            'instagram_link',
            'twitter_link',
        ]