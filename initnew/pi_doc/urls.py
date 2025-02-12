from django.urls import path
from .views import pi_doc_view, section_detail_view, pdf_upload_view, section_list_view, documents_by_year_view

urlpatterns = [
    path('', section_list_view, name='section_list_view'),
    path('section/<int:section_id>/', section_detail_view, name='section_detail_view'),
    path('upload/', pdf_upload_view, name='pdf_upload_view'),
    path('pi_doc/', pi_doc_view, name='pi_doc_view'),
    path('year/<int:year>/', documents_by_year_view, name='documents_by_year_view'),  # Новый путь
]
