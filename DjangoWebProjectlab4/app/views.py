"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpRequest, HttpResponseRedirect
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def newpost(request):
    if not request.user.is_superuser:
        return redirect('blog')
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'app/newpost.html', {'form': form})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )
def links(request):
    assert isinstance(request, HttpRequest)
    return render(request, 
                  'app/links.html',
                  {
                    'title': 'Ссылки',  # Заголовок страницы
                    'links': [  # Список ссылок
                        {
                            'name': 'NASA',
                            'url': 'https://www.nasa.gov',
                        },
                        {
                            'name': 'Space.com',
                            'url': 'https://www.space.com',
                        },
                        {
                            'name': 'ESO',
                            'url': 'https://www.eso.org',
                        }
                    ],
                    'year': datetime.now().year,  # Текущий год
                  }
    )
def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            rating = form.cleaned_data['rating']
            interests = form.cleaned_data.get('interests', [])
            source = form.cleaned_data['source']
            comment = form.cleaned_data['comment']

            # Вывод данных (можно сохранить в БД)
            return render(request, 'app/pool.html', {
                'submitted': True,
                'name': name,
                'email': email,
                'rating': rating,
                'interests': interests,
                'source': source,
                'comment': comment,
            })
    else:
        form = FeedbackForm()

    return render(request, 'app/pool.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/registration.html', {'form': form})


def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()  # Запрос всех статей блога
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)  # Запрос конкретной статьи
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'year': datetime.now().year,
        }
    )


def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )

def videopost(request):
    return render(request, 'app/videopost.html')


