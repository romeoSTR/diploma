from django import forms

from .models import UserProfile, FilmComment, Series, FilmReview


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'username', 'password', 'email', 'birthday', 'about', 'photo'
        ]
        labels = [
            'Логин', 'Пароль', 'е-mail', 'Дата рождения', 'О себе', 'Фото'
        ]
        widgets = {'birthday': DateInput()}


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = FilmComment
        fields = [
            'text'
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = FilmReview
        fields = [
            'text', 'is_positive'
        ]