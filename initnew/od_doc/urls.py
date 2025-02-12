from django.urls import path
from . import views

urlpatterns = [
    path('', views.od_doc_view, name='od_doc_view'),  # Исправлено имя функции представления
    path('section/<int:section_id>/', views.od_section_detail_view, name='od_section_detail_view'),
    path('sections/', views.od_section_list_view, name='od_section_list_view'),
    path('upload/', views.od_pdf_upload_view, name='od_pdf_upload_view'),
    path('documents/<int:year>/', views.od_documents_by_year_view, name='od_documents_by_year_view'),
    
]
