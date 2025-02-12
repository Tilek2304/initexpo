from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import DepartmentOD, TeacherOD, AboutspiOD, ContactOD, AwardOD
from od_doc.models import Section  # Измененная строка

# Create your views here.

def home(request):
    about_info = AboutspiOD.objects.first()
    sort_by = request.GET.get('sort', 'last_name')
    teacher_list = TeacherOD.objects.filter(is_active=True).order_by(sort_by)
    paginator = Paginator(teacher_list, 8)  # Показать 8 преподавателей на странице
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)
    head_of_department = TeacherOD.objects.filter(position='Заведующий кафедрой', is_active=True).first()
    other_teachers = TeacherOD.objects.filter(is_active=True).exclude(position='Заведующий кафедрой')[:3]
    sections = Section.objects.all()
    awards = AwardOD.objects.all()
    sectionsOD = Section.objects.all()  # Новая строка

    return render(request, 'kafedra_home_od.html', {
        'about_info': about_info,
        'teachers': teachers,
        'head_of_department': head_of_department,
        'other_teachers': other_teachers,
        'sections': sections,
        'awards': awards,
        'sectionsod': sectionsOD,  # Новая строка
    })

def department_list(request):
    departments = DepartmentOD.objects.all()
    return render(request, 'department_list_od.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(DepartmentOD, id=id)
    context = {
        'department': department,
        'image': 'kafedra_od/images/department.jpg'  # Замените на фактическое изображение
    }
    return render(request, 'department_detail_od.html', context)

def teacher_list(request):
    teachers = TeacherOD.objects.all()
    return render(request, 'teacher_list_od.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(TeacherOD, id=id)
    return render(request, 'teacher_detail_od.html', {'teacher': teacher})

def about(request):
    about_info = AboutspiOD.objects.first()
    if not about_info:
        about_info = AboutspiOD.objects.create(title="Default Title", content="Default Content")
    return render(request, 'about_od.html', {'about_info': about_info})

def contacts(request):
    contact_info = ContactOD.objects.first()
    return render(request, 'contacts_od.html', {'contact_info': contact_info})
