from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    def save(self):
        user = super().save()
        profile = Profile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')
    def clean_answer(self):
        if self.cleaned_data.get('answer', None) != 6:
            raise forms.ValidationError('땡~!!!')


