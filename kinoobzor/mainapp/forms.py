from django import forms

from .models import UserProfile


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'username', 'password', 'email', 'birthday', 'about', 'photo'
        ]
        widgets = {'birthday': DateInput()}