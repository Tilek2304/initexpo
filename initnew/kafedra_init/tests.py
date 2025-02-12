from django.test import TestCase
from .models import DepartmentINIT, TeacherINIT, AboutspiINIT, ContactINIT

# Create your tests here.

class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/kafedra_init/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_home_init.html')

class DepartmentListViewTests(TestCase):
    def test_department_list_view(self):
        response = self.client.get('/kafedra_init/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_list_init.html')

class DepartmentDetailViewTests(TestCase):
    def test_department_detail_view(self):
        department = DepartmentINIT.objects.create(name='Test Department', description='Test Description')
        response = self.client.get(f'/kafedra_init/departments/{department.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_detail_init.html')
        self.assertContains(response, department.name)
        self.assertContains(response, department.description)

class TeacherListViewTests(TestCase):
    def test_teacher_list_view(self):
        response = self.client.get('/kafedra_init/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_list_init.html')

class TeacherDetailViewTests(TestCase):
    def test_teacher_detail_view(self):
        teacher = TeacherINIT.objects.create(first_name='Test', last_name='Teacher', bio='Test Bio')
        response = self.client.get(f'/kafedra_init/teachers/{teacher.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_detail_init.html')
        self.assertContains(response, teacher.first_name)
        self.assertContains(response, teacher.last_name)
        self.assertContains(response, teacher.bio)

class AboutViewTests(TestCase):
    def test_about_view(self):
        about_info = AboutspiINIT.objects.create(title='About Title', content='About Content')
        response = self.client.get('/kafedra_init/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_init.html')
        self.assertContains(response, about_info.title)
        self.assertContains(response, about_info.content)

class ContactsViewTests(TestCase):
    def test_contacts_view(self):
        contact_info = ContactINIT.objects.create(title='Contact Title', content='Contact Content')
        response = self.client.get('/kafedra_init/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts_init.html')
        self.assertContains(response, contact_info.title)
        self.assertContains(response, contact_info.content)
