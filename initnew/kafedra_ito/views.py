from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import DepartmentITO, TeacherITO, AboutspiITO, ContactITO, AwardITO
from ito_doc.models import Section  # Измененная строка

# Create your views here.

def home(request):
    about_info = AboutspiITO.objects.first()
    sort_by = request.GET.get('sort', 'last_name')
    teacher_list = TeacherITO.objects.filter(is_active=True).order_by(sort_by)
    paginator = Paginator(teacher_list, 8)  # Показать 8 преподавателей на странице
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)
    head_of_department = TeacherITO.objects.filter(position='Заведующий кафедрой', is_active=True).first()
    other_teachers = TeacherITO.objects.filter(is_active=True).exclude(position='Заведующий кафедрой')[:3]
    sections = Section.objects.all()
    awards = AwardITO.objects.all()
    sectionsito = Section.objects.all()  # Новая строка

    return render(request, 'kafedra_home_ito.html', {
        'about_info': about_info,
        'teachers': teachers,
        'head_of_department': head_of_department,
        'other_teachers': other_teachers,
        'sections': sections,
        'awards': awards,
        'sectionsito': sectionsito,  # Новая строка
    })

def department_list(request):
    departments = DepartmentITO.objects.all()
    return render(request, 'department_list_ito.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(DepartmentITO, id=id)
    context = {
        'department': department,
        'image': 'kafedra_ito/images/department.jpg'  # Замените на фактическое изображение
    }
    return render(request, 'department_detail_ito.html', context)

def teacher_list(request):
    teachers = TeacherITO.objects.all()
    return render(request, 'teacher_list_ito.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(TeacherITO, id=id)
    return render(request, 'teacher_detail_ito.html', {'teacher': teacher})

def about(request):
    about_info = AboutspiITO.objects.first()
    if not about_info:
        about_info = AboutspiITO.objects.create(title="Default Title", content="Default Content")
    return render(request, 'about_ito.html', {'about_info': about_info})

def contacts(request):
    contact_info = ContactITO.objects.first()
    return render(request, 'contacts_ito.html', {'contact_info': contact_info})
