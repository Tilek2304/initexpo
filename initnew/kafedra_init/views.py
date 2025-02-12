from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import DepartmentINIT, TeacherINIT, AboutspiINIT, ContactINIT, AwardINIT
from init_doc.models import Section  # Измененная строка

# Create your views here.

def home(request):
    about_info = AboutspiINIT.objects.first()
    sort_by = request.GET.get('sort', 'last_name')
    teacher_list = TeacherINIT.objects.filter(is_active=True).order_by(sort_by)
    paginator = Paginator(teacher_list, 8)  # Показать 8 преподавателей на странице
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)
    head_of_department = TeacherINIT.objects.filter(position='Заведующий кафедрой', is_active=True).first()
    other_teachers = TeacherINIT.objects.filter(is_active=True).exclude(position='Заведующий кафедрой')[:3]
    sections = Section.objects.all()
    awards = AwardINIT.objects.all()
    sectionsINIT = Section.objects.all()  # Новая строка

    return render(request, 'kafedra_home_init.html', {
        'about_info': about_info,
        'teachers': teachers,
        'head_of_department': head_of_department,
        'other_teachers': other_teachers,
        'sections': sections,
        'awards': awards,
        'sectionsinit': sectionsINIT,  # Новая строка
    })

def department_list(request):
    departments = DepartmentINIT.objects.all()
    return render(request, 'department_list_init.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(DepartmentINIT, id=id)
    context = {
        'department': department,
        'image': 'kafedra_init/images/department.jpg'  # Замените на фактическое изображение
    }
    return render(request, 'department_detail_init.html', context)

def teacher_list(request):
    teachers = TeacherINIT.objects.all()
    return render(request, 'teacher_list_init.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(TeacherINIT, id=id)
    return render(request, 'teacher_detail_init.html', {'teacher': teacher})

def about(request):
    about_info = AboutspiINIT.objects.first()
    if not about_info:
        about_info = AboutspiINIT.objects.create(title="Default Title", content="Default Content")
    return render(request, 'about_init.html', {'about_info': about_info})

def contacts(request):
    contact_info = ContactINIT.objects.first()
    return render(request, 'contacts_init.html', {'contact_info': contact_info})
