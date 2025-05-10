from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Feedback

User = get_user_model()

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="Имя")
    last_name = forms.CharField(max_length=30, label="Фамилия")
    age = forms.IntegerField(label="Возраст", required=False)
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Напишите о себе...', 'class': 'form-control'}),
        label="Биография",
        required=False
    )
    avatar = forms.ImageField(label="Аватар", required=False)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.cleaned_data.get('age')
        user.bio = self.cleaned_data.get('bio')
        user.avatar = self.cleaned_data.get('avatar')
        user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'bio', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
        }
        labels = {
            'name': 'Имя',
            'comment': 'Комментарий',
        }
