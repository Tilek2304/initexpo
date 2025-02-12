from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class PiDocViewTests(TestCase):
    def test_pi_doc_view(self):
        response = self.client.get(reverse('pi_doc_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pi_doc/pi_doc.html')
    
    def test_documents_by_year_view(self):
        response = self.client.get(reverse('documents_by_year_view', args=[2025]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pi_doc/documents_by_year.html')
