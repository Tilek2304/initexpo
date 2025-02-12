from django.test import TestCase
from .models import Department, Teacher, Aboutspi, Contact

# Create your tests here.

class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/kafedra_pi/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/kafedra_home.html')

    def test_kafedra_pi_view(self):
        response = self.client.get('/kafedra_pi/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/kafedra_home.html')

class DepartmentListViewTests(TestCase):
    def test_department_list_view(self):
        response = self.client.get('/kafedra_pi/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/department_list.html')

class DepartmentDetailViewTests(TestCase):
    def test_department_detail_view(self):
        department = Department.objects.create(name='Test Department', description='Test Description')
        response = self.client.get(f'/kafedra_pi/departments/{department.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/department_detail.html')
        self.assertContains(response, department.name)
        self.assertContains(response, department.description)

class TeacherListViewTests(TestCase):
    def test_teacher_list_view(self):
        response = self.client.get('/kafedra_pi/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/teacher_list.html')

class TeacherDetailViewTests(TestCase):
    def test_teacher_detail_view(self):
        teacher = Teacher.objects.create(name='Test Teacher', bio='Test Bio')
        response = self.client.get(f'/kafedra_pi/teachers/{teacher.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/teacher_detail.html')
        self.assertContains(response, teacher.name)
        self.assertContains(response, teacher.bio)

class AboutViewTests(TestCase):
    def test_about_view(self):
        abouts = Aboutspi.objects.create(title='About Title', content='About Content')
        response = self.client.get('/kafedra_pi/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/about.html')
        self.assertContains(response, abouts.title)
        self.assertContains(response, abouts.content)

class ContactsViewTests(TestCase):
    def test_contacts_view(self):
        response = self.client.get('/kafedra_pi/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kafedra_pi/contacts.html')
