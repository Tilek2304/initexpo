# urls.py
from django.urls import path
from .views import index, about, home, popup_menu, news_home

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),  # Добавлено
    path('popup_menu/', popup_menu, name='popup_menu'),
    path('news_home/', news_home, name='news_home'),
    # Other URL patterns
]
