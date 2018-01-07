from django import forms


class TwitterUsernameForm(forms.Form):
    username = forms.CharField(label='twitter-username', max_length=256)
