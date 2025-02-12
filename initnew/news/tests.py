from django.test import TestCase
from django.urls import reverse
from .models import Articles

class AboutUsViewTest(TestCase):
    def test_about_us_view(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/about_us.html')

class NewsViewsTest(TestCase):
    def setUp(self):
        self.article = Articles.objects.create(
            title="Test Article",
            anons="Test Anons",
            full_text="Test Full Text",
            author="Test Author"
        )

    def test_news_home_view(self):
        response = self.client.get(reverse('news_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_home.html')

    def test_news_detail_view(self):
        response = self.client.get(reverse('news_detail_view', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_detail_view.html')

    def test_create_news_view(self):
        response = self.client.get(reverse('create_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/create_news.html')

    def test_edit_news_view(self):
        response = self.client.get(reverse('edit_news', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/edit_news.html')

class ErrorViewsTest(TestCase):
    def test_404_error_view(self):
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_500_error_view(self):
        response = self.client.get(reverse('trigger_500_error'))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, '500.html')
