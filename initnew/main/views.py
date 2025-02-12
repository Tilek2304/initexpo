from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import SliderImage, GalleryImage, Articles, About  # Обновлено с AboutUs на About
from pi_doc.models import Section, Document  # Импортировать модели Section и Document
from ito_doc.models import Section as SectionITO  # Импортировать модель Section из ito_doc

def index(request):
    slider_images = SliderImage.objects.filter(is_active=True)[:4]
    gallery_images = GalleryImage.objects.filter(is_active=True)
    articles = Articles.objects.all()[:5]
    contest_start_date = datetime(2025, 5, 1, 10, 0)
    about = About.objects.first()  # Обновлено с AboutUs на About
    sections = Section.objects.all()  # Добавить эту строку для получения данных секций
    documents = Document.objects.all()  # Добавить эту строку для получения данных документов
    sectionsito = SectionITO.objects.all()  # Добавить эту строку для получения данных секций ИТО
    
    context = {
        'slider_images': slider_images,
        'gallery_images': gallery_images,
        'articles': articles,
        'contest_start_date': contest_start_date,
        'about': about,  # Обновлено с AboutUs на About
        'sections': sections,  # Добавить секции в контекст
        'documents': documents,  # Добавить документы в контекст
        'sectionsito': sectionsito,  # Добавить секции ИТО в контекст
    }
    return render(request, 'main/home.html', context)  # Изменено с 'main/index.html' на 'main/home.html'

def about(request):
    about = About.objects.first()  # Обновлено с AboutUs на About
    return render(request, 'main/about.html', {'about': about})  # Исправлено 'about_info' на 'about'

def home(request):
    slider_images = SliderImage.objects.filter(is_active=True)[:4]
    gallery_images = GalleryImage.objects.filter(is_active=True)
    articles = Articles.objects.all()[:5]
    contest_start_date = datetime(2025, 5, 1, 10, 0)
    about = About.objects.first()  # Обновлено с AboutUs на About
    sections = Section.objects.all()  # Добавить эту строку для получения данных секций
    documents = Document.objects.all()  # Добавить эту строку для получения данных документов
    sectionsito = SectionITO.objects.all()  # Добавить эту строку для получения данных секций ИТО
    
    context = {
        'slider_images': slider_images,
        'gallery_images': gallery_images,
        'articles': articles,
        'contest_start_date': contest_start_date,
        'about': about,  # Обновлено с AboutUs на About
        'sections': sections,  # Добавить секции в контекст
        'documents': documents,  # Добавить документы в контекст
        'sectionsito': sectionsito,  # Добавить секции ИТО в контекст
    }
    return render(request, 'main/home.html', context)  # Исправлено 'main/index.html' на 'main/home.html'

def popup_menu(request):
    return render(request, 'main/popup_menu.html')

def news_home(request):
    articles = Articles.objects.all()
    return render(request, 'main/news_home.html', {'articles': articles})



