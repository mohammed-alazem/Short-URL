from django import forms

from .models import Shortener


class ShortenerForm(forms.ModelForm):
    LongURL = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener

        fields = ('LongURL',)
