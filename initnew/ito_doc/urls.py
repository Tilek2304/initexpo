from django.urls import path
from . import views

urlpatterns = [
    path('', views.ito_doc_view, name='ito_doc_view'),
    path('section/<int:section_id>/', views.ito_section_detail_view, name='ito_section_detail_view'),
    path('sections/', views.ito_section_list_view, name='ito_section_list_view'),
    path('upload/', views.ito_pdf_upload_view, name='ito_pdf_upload_view'),
    path('documents/<int:year>/', views.ito_documents_by_year_view, name='ito_documents_by_year_view'),
    
]
