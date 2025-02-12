from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, PDFDocument
from .forms import PDFDocumentForm
from datetime import datetime

# Create your views here.

def pi_doc_view(request):
    sections = Section.objects.all()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'pi_doc/pi_doc.html', {'sections': sections, 'years': years})

def section_detail_view(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    sections = Section.objects.all()
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
    return render(request, 'pi_doc/section_detail.html', {
        'section': section,
        'pdfs': pdfs,
        'years': years,
        'selected_year': year,
        'sections': sections
    })

def section_list_view(request):
    sections = Section.objects.all()
    current_year = datetime.now().year
    year = request.GET.get('year', current_year)
    sections = Section.objects.filter(pdfdocument__year=year).distinct()
    years = PDFDocument.objects.values_list('year', flat=True).distinct()
    return render(request, 'pi_doc/section_list.html', {
        'sections': sections,
        'years': years,
        'selected_year': int(year)
    })

def pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('section_list_view')
    else:
        form = PDFDocumentForm()
    return render(request, 'pi_doc/pdf_upload.html', {'form': form})

def documents_by_year_view(request, year):
    documents = PDFDocument.objects.filter(year=year)
    return render(request, 'pi_doc/documents_by_year.html', {'documents': documents, 'year': year})
