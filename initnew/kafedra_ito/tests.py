from django.test import TestCase
from .models import DepartmentITO, TeacherITO, AboutspiITO, ContactITO

# Create your tests here.

class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/kafedra_ito/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_home_ito.html')

class DepartmentListViewTests(TestCase):
    def test_department_list_view(self):
        response = self.client.get('/kafedra_ito/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_list_ito.html')

class DepartmentDetailViewTests(TestCase):
    def test_department_detail_view(self):
        department = DepartmentITO.objects.create(name='Test Department', description='Test Description')
        response = self.client.get(f'/kafedra_ito/departments/{department.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_detail_ito.html')
        self.assertContains(response, department.name)
        self.assertContains(response, department.description)

class TeacherListViewTests(TestCase):
    def test_teacher_list_view(self):
        response = self.client.get('/kafedra_ito/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_list_ito.html')

class TeacherDetailViewTests(TestCase):
    def test_teacher_detail_view(self):
        teacher = TeacherITO.objects.create(first_name='Test', last_name='Teacher', bio='Test Bio')
        response = self.client.get(f'/kafedra_ito/teachers/{teacher.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_detail_ito.html')
        self.assertContains(response, teacher.first_name)
        self.assertContains(response, teacher.last_name)
        self.assertContains(response, teacher.bio)

class AboutViewTests(TestCase):
    def test_about_view(self):
        about_info = AboutspiITO.objects.create(title='About Title', content='About Content')
        response = self.client.get('/kafedra_ito/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_ito.html')
        self.assertContains(response, about_info.title)
        self.assertContains(response, about_info.content)

class ContactsViewTests(TestCase):
    def test_contacts_view(self):
        contact_info = ContactITO.objects.create(title='Contact Title', content='Contact Content')
        response = self.client.get('/kafedra_ito/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts_ito.html')
        self.assertContains(response, contact_info.title)
        self.assertContains(response, contact_info.content)
