from django.test import TestCase
from .models import DepartmentOSPO, TeacherOSPO, AboutspiOSPO, ContactOSPO

# Create your tests here.

class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/kafedra_ospo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_home_ospo.html')

class DepartmentListViewTests(TestCase):
    def test_department_list_view(self):
        response = self.client.get('/kafedra_ospo/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_list_ospo.html')

class DepartmentDetailViewTests(TestCase):
    def test_department_detail_view(self):
        department = DepartmentOSPO.objects.create(name='Test Department', description='Test Description')
        response = self.client.get(f'/kafedra_ospo/departments/{department.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department_detail_ospo.html')
        self.assertContains(response, department.name)
        self.assertContains(response, department.description)

class TeacherListViewTests(TestCase):
    def test_teacher_list_view(self):
        response = self.client.get('/kafedra_ospo/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_list_ospo.html')

class TeacherDetailViewTests(TestCase):
    def test_teacher_detail_view(self):
        teacher = TeacherOSPO.objects.create(first_name='Test', last_name='Teacher', bio='Test Bio')
        response = self.client.get(f'/kafedra_ospo/teachers/{teacher.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_detail_ospo.html')
        self.assertContains(response, teacher.first_name)
        self.assertContains(response, teacher.last_name)
        self.assertContains(response, teacher.bio)

class AboutViewTests(TestCase):
    def test_about_view(self):
        about_info = AboutspiOSPO.objects.create(title='About Title', content='About Content')
        response = self.client.get('/kafedra_ospo/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_ospo.html')
        self.assertContains(response, about_info.title)
        self.assertContains(response, about_info.content)

class ContactsViewTests(TestCase):
    def test_contacts_view(self):
        contact_info = ContactOSPO.objects.create(title='Contact Title', content='Contact Content')
        response = self.client.get('/kafedra_ospo/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts_ospo.html')
        self.assertContains(response, contact_info.title)
        self.assertContains(response, contact_info.content)
