from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, AvatarUser, BackgroundUser


class CustomUserCreationForm(UserCreationForm):
    """User registration form class"""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class UserProfileForm(forms.ModelForm):
    """Form class for changing username"""
    
    class Meta:
        model = User
        fields = ['username']
        labels = {'username': 'Нікнейм'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user_form_edit-label_username'})
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False


class AvatarUserForm(forms.ModelForm):
    """Form class for changing the avatar"""

    class Meta:
        model = AvatarUser
        fields = ['avatar']
        labels = {'avatar': 'Аватар'}
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'input-file-avatar'})
        }

    def __init__(self, *args, **kwargs):
        super(AvatarUserForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False


class BackgroundForm(forms.ModelForm):
    """Form class for changing the background"""

    class Meta:
        model = BackgroundUser
        fields = ['background']
        labels = {'background': 'Фонова фотографія'}
        widgets = {
            'background': forms.FileInput(attrs={'class': 'input-file-background'})
        }

    def __init__(self, *args, **kwargs):
        super(BackgroundForm, self).__init__(*args, **kwargs)
        self.fields['background'].required = False
