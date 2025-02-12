from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kafedra_home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('aboutpi/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
