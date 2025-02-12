from django.urls import path
from . import views

urlpatterns = [
    path('', views.ospo_doc_view, name='ospo_doc_view'),  # Исправлено имя функции представления
    path('section/<int:section_id>/', views.ospo_section_detail_view, name='ospo_section_detail_view'),
    path('sections/', views.ospo_section_list_view, name='ospo_section_list_view'),
    path('upload/', views.ospo_pdf_upload_view, name='ospo_pdf_upload_view'),
    path('documents/<int:year>/', views.ospo_documents_by_year_view, name='ospo_documents_by_year_view'),
    
]
