"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Blog, Comment
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'short_content', 'image', 'full_content')
        labels = {
            'title': 'Заголовок',
            'short_content': 'Краткое содержание',
            'image': 'Изображение',
            'full_content': 'Полное содержание',
        }

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    
class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    rating = forms.ChoiceField(
        label="Оценка сайта",
        choices=[
            ('5', '5 (Отлично)'),
            ('4', '4 (Хорошо)'),
            ('3', '3 (Удовлетворительно)'),
            ('2', '2 (Плохо)'),
            ('1', '1 (Ужасно)'),
        ],
        widget=forms.RadioSelect,
        required=True,
    )
    interests = forms.MultipleChoiceField(
        label="Что вам интересно?",
        choices=[
            ('stars', 'Звёзды'),
            ('planets', 'Планеты'),
            ('galaxies', 'Галактики'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    source = forms.ChoiceField(
        label="Как вы узнали о нас?",
        choices=[
            ('search', 'Поисковик (Google, Яндекс)'),
            ('social', 'Соцсети'),
            ('friend', 'От друзей'),
        ],
        required=True,
    )
    comment = forms.CharField(
        label="Ваши пожелания",
        widget=forms.Textarea,
        required=False,
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}
