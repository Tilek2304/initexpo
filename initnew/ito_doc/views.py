from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, PDFDocument
from .forms import PDFDocumentForm
from datetime import datetime

# Представление для главной страницы документов ITO
def ito_doc_view(request):
    sectionsito = Section.objects.all()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'ito/ito_doc.html', {'sectionsito': sectionsito, 'years': years})

# Представление для детального просмотра секции
def ito_section_detail_view(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    sectionsito = Section.objects.all()
    current_year = datetime.now().year
    year = request.GET.get('year', current_year)

    if year:
        try:
            year = int(year)
        except ValueError:
            year = None

    pdfs = PDFDocument.objects.filter(section=section)
    if year:
        pdfs = pdfs.filter(year=year)

    years = PDFDocument.objects.filter(section=section).values_list('year', flat=True).distinct()
    return render(request, 'ito/ito_section_detail.html', {
        'section': section,
        'pdfs': pdfs,
        'years': years,
        'selected_year': year,
        'sectionsito': sectionsito
    })

# Представление для списка секций
def ito_section_list_view(request):
    sectionsito = Section.objects.all()
    current_year = datetime.now().year
    year = request.GET.get('year', current_year)
    sectionsito = Section.objects.filter(pdfdocument__year=year).distinct()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'ito/ito_section_list.html', {
        'sectionsito': sectionsito,
        'years': years,
        'selected_year': int(year)
    })

# Представление для загрузки PDF
def ito_pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ito_section_list_view')
    else:
        form = PDFDocumentForm()
    return render(request, 'ito/ito_pdf_upload.html', {'form': form})

# Представление для просмотра документов по году
def ito_documents_by_year_view(request, year):
    pdfdocuments = PDFDocument.objects.filter(year=year)  # Измененная строка
    return render(request, 'ito/ito_documents_by_year.html', {'pdfdocuments': pdfdocuments, 'year': year})  # Измененная строка

