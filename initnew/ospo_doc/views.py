from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, PDFDocument
from .forms import PDFDocumentForm
from datetime import datetime

# Представление для главной страницы документов OSPO
def ospo_doc_view(request):
    sectionsospo = Section.objects.all()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'ospo/ospo_doc.html', {'sectionsospo': sectionsospo, 'years': years})

# Представление для детального просмотра секции
def ospo_section_detail_view(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    sectionsospo = Section.objects.all()
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
    return render(request, 'ospo/ospo_section_detail.html', {
        'section': section,
        'pdfs': pdfs,
        'years': years,
        'selected_year': year,
        'sectionsospo': sectionsospo,
    })

# Представление для списка секций
def ospo_section_list_view(request):
    sectionsospo = Section.objects.all()
    current_year = datetime.now().year
    year = request.GET.get('year', current_year)
    sectionsospo = Section.objects.filter(pdfdocument__year=year).distinct()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'ospo/ospo_section_list.html', {
        'sectionsospo': sectionsospo,
        'years': years,
        'selected_year': int(year)
    })

# Представление для загрузки PDF
def ospo_pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ospo_section_list_view')
    else:
        form = PDFDocumentForm()
    return render(request, 'ospo/ospo_pdf_upload.html', {'form': form})

# Представление для просмотра документов по году
def ospo_documents_by_year_view(request, year):
    pdfdocuments = PDFDocument.objects.filter(year=year)
    return render(request, 'ospo/ospo_documents_by_year.html', {'pdfdocuments': pdfdocuments, 'year': year})