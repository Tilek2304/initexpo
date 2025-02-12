from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_doc_view, name='init_doc_view'),  # Исправлено имя функции представления
    path('section/<int:section_id>/', views.init_section_detail_view, name='init_section_detail_view'),
    path('sections/', views.init_section_list_view, name='init_section_list_view'),
    path('upload/', views.init_pdf_upload_view, name='init_pdf_upload_view'),
    path('documents/<int:year>/', views.init_documents_by_year_view, name='init_documents_by_year_view'),
    
]
