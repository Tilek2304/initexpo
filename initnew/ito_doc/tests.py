from django.test import TestCase
from django.urls import reverse
from .models import PDFDocument, Section

class PDFDocumentDeleteViewTest(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name="Test Section")
        self.pdf_document = PDFDocument.objects.create(
            title="Test PDF",
            section=self.section,
            year=2023,
            file="test.pdf"
        )

    def test_delete_pdf_document(self):
        response = self.client.post(reverse('ito_pdf_delete_view', args=[self.pdf_document.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(PDFDocument.objects.filter(id=self.pdf_document.id).exists())

class PDFDocumentEditViewTest(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name="Test Section")
        self.pdf_document = PDFDocument.objects.create(
            title="Test PDF",
            section=self.section,
            year=2023,
            file="test.pdf"
        )

    def test_edit_pdf_document(self):
        response = self.client.post(reverse('ito_pdf_edit_view', args=[self.pdf_document.id]), {
            'title': 'Updated Test PDF',
            'section': self.section.id,
            'year': 2023,
            'file': self.pdf_document.file
        })
        self.assertEqual(response.status_code, 302)
        self.pdf_document.refresh_from_db()
        self.assertEqual(self.pdf_document.title, 'Updated Test PDF')

    def test_edit_pdf_document_with_description(self):
        response = self.client.post(reverse('ito_pdf_edit_view', args=[self.pdf_document.id]), {
            'title': 'Updated Test PDF',
            'section': self.section.id,
            'year': 2023,
            'file': self.pdf_document.file,
            'description': 'Updated description'
        })
        self.assertEqual(response.status_code, 302)
        self.pdf_document.refresh_from_db()
        self.assertEqual(self.pdf_document.description, 'Updated description')

class SectionListViewTest(TestCase):
    def setUp(self):
        self.section1 = Section.objects.create(name="Section 1")
        self.section2 = Section.objects.create(name="Section 2")
        PDFDocument.objects.create(title="PDF 1", section=self.section1, year=2022, file="pdf1.pdf")
        PDFDocument.objects.create(title="PDF 2", section=self.section2, year=2023, file="pdf2.pdf")

    def test_section_list_view_filters_by_year(self):
        response = self.client.get(reverse('ito_section_list_view'), {'year': 2022})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section 1")
        self.assertNotContains(response, "Section 2")

        response = self.client.get(reverse('ito_section_list_view'), {'year': 2023})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section 2")
        self.assertNotContains(response, "Section 1")
