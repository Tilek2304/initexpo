from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Department, Teacher, Aboutspi, Contact, Award  # Импортировать модель Award
from pi_doc.models import Section, Document  # Импортировать модели Section и Document

# Create your views here.

def home(request):
    about_info = Aboutspi.objects.first()
    sort_by = request.GET.get('sort', 'last_name')
    teacher_list = Teacher.objects.filter(is_active=True).order_by(sort_by)
    paginator = Paginator(teacher_list, 8)  # Показать 8 преподавателей на странице
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)
    head_of_department = Teacher.objects.filter(position='Заведующий кафедрой', is_active=True).first()
    other_teachers = Teacher.objects.filter(is_active=True).exclude(position='Заведующий кафедрой')[:3]
    sections = Section.objects.all()  # Добавить эту строку для получения данных секций
    documents = Document.objects.all()  # Добавить эту строку для получения данных документов
    awards = Award.objects.all()  # Добавить эту строку для получения данных наград

    return render(request, 'kafedra_pi/kafedra_home.html', {
        'about_info': about_info,
        'teachers': teachers,
        'head_of_department': head_of_department,
        'other_teachers': other_teachers,
        'sections': sections,  # Добавить секции в контекст
        'documents': documents,  # Добавить документы в контекст
        'awards': awards,  # Добавить награды в контекст
    })

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'kafedra_pi/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    context = {
        'department': department,
        'image': 'kafedra_pi/images/department.jpg'  # Замените на фактическое изображение
    }
    return render(request, 'kafedra_pi/department_detail.html', context)

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'kafedra_pi/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'kafedra_pi/teacher_detail.html', {'teacher': teacher})

def about(request):
    about_info = Aboutspi.objects.first()
    if not about_info:
        about_info = Aboutspi.objects.create(title="Default Title", content="Default Content")
    return render(request, 'kafedra_pi/about.html', {'about_info': about_info})

def contacts(request):
    contact_info = Contact.objects.first()
    return render(request, 'kafedra_pi/contacts.html', {'contact_info': contact_info})
