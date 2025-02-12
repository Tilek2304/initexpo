from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import DepartmentOSPO, TeacherOSPO, AboutspiOSPO, ContactOSPO, AwardOSPO
from ospo_doc.models import Section  # Измененная строка

# Create your views here.

def home(request):
    about_info = AboutspiOSPO.objects.first()
    sort_by = request.GET.get('sort', 'last_name')
    teacher_list = TeacherOSPO.objects.filter(is_active=True).order_by(sort_by)
    paginator = Paginator(teacher_list, 8)  # Показать 8 преподавателей на странице
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)
    head_of_department = TeacherOSPO.objects.filter(position='Заведующий кафедрой', is_active=True).first()
    other_teachers = TeacherOSPO.objects.filter(is_active=True).exclude(position='Заведующий кафедрой')[:3]
    sections = Section.objects.all()
    awards = AwardOSPO.objects.all()
    sectionsOSPO = Section.objects.all()  # Новая строка

    return render(request, 'kafedra_home_ospo.html', {
        'about_info': about_info,
        'teachers': teachers,
        'head_of_department': head_of_department,
        'other_teachers': other_teachers,
        'sections': sections,
        'awards': awards,
        'sectionsospo': sectionsOSPO,  # Новая строка
    })

def department_list(request):
    departments = DepartmentOSPO.objects.all()
    return render(request, 'department_list_ospo.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(DepartmentOSPO, id=id)
    context = {
        'department': department,
        'image': 'kafedra_ospo/images/department.jpg'  # Замените на фактическое изображение
    }
    return render(request, 'department_detail_ospo.html', context)

def teacher_list(request):
    teachers = TeacherOSPO.objects.all()
    return render(request, 'teacher_list_ospo.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(TeacherOSPO, id=id)
    return render(request, 'teacher_detail_ospo.html', {'teacher': teacher})

def about(request):
    about_info = AboutspiOSPO.objects.first()
    if not about_info:
        about_info = AboutspiOSPO.objects.create(title="Default Title", content="Default Content")
    return render(request, 'about_ospo.html', {'about_info': about_info})

def contacts(request):
    contact_info = ContactOSPO.objects.first()
    return render(request, 'contacts_ospo.html', {'contact_info': contact_info})
