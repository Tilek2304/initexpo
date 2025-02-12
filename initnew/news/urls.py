from django.urls import path, include  # Импортируйте include
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail_view'),  # Убедитесь, что здесь имя 'news_detail_view'
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Это корректная строка для CKEditor
]
