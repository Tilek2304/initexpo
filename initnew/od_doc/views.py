from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, PDFDocument
from .forms import PDFDocumentForm
from datetime import datetime

# Представление для главной страницы документов od
def od_doc_view(request):
    sectionsod = Section.objects.all()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'od/od_doc.html', {'sectionsod': sectionsod, 'years': years})

# Представление для детального просмотра секции
def od_section_detail_view(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    sectionsod = Section.objects.all()
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
    return render(request, 'od/od_section_detail.html', {
        'section': section,
        'pdfs': pdfs,
        'years': years,
        'selected_year': year,
        'sectionsod': sectionsod,
    })

# Представление для списка секций
def od_section_list_view(request):
    sectionsod = Section.objects.all()
    current_year = datetime.now().year
    year = request.GET.get('year', current_year)
    sectionsod = Section.objects.filter(pdfdocument__year=year).distinct()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'od/od_section_list.html', {
        'sectionsod': sectionsod,
        'years': years,
        'selected_year': int(year)
    })

# Представление для загрузки PDF
def od_pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('od_section_list_view')
    else:
        form = PDFDocumentForm()
    return render(request, 'od/od_pdf_upload.html', {'form': form})

# Представление для просмотра документов по году
def od_documents_by_year_view(request, year):
    pdfdocuments = PDFDocument.objects.filter(year=year)
    return render(request, 'od/od_documents_by_year.html', {'pdfdocuments': pdfdocuments, 'year': year})