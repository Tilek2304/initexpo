from django.test import TestCase
from django.urls import reverse
from .models import PDFDocument, Section

class SectionListViewTest(TestCase):
    def setUp(self):
        self.section1 = Section.objects.create(name="Section 1")
        self.section2 = Section.objects.create(name="Section 2")
        PDFDocument.objects.create(title="PDF 1", section=self.section1, year=2022, file="pdf1.pdf", description="Description 1")
        PDFDocument.objects.create(title="PDF 2", section=self.section2, year=2023, file="pdf2.pdf", description="Description 2")

    def test_section_list_view_filters_by_year(self):
        response = self.client.get(reverse('init_section_list_view'), {'year': 2022})                                  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section 1")
        self.assertNotContains(response, "Section 2")

        response = self.client.get(reverse('init_section_list_view'), {'year': 2023})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section 2")
        self.assertNotContains(response, "Section 1")
        
    def test_pdf_document_description(self):
        pdf1 = PDFDocument.objects.get(title="PDF 1")
        pdf2 = PDFDocument.objects.get(title="PDF 2")
        self.assertEqual(pdf1.description, "Description 1")
        self.assertEqual(pdf2.description, "Description 2")
