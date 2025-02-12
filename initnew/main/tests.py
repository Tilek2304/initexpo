from django.test import TestCase
from .models import Articles, SliderImage, GalleryImage, About

class ModelTestCase(TestCase):
    def setUp(self):
        self.article = Articles.objects.create(
            title="Test Article",
            anons="Test Anons",
            full_text="Test Full Text"
        )
        self.slider_image = SliderImage.objects.create(
            title="Test Slider",
            image="test_slider.jpg"
        )
        self.gallery_image = GalleryImage.objects.create(
            title="Test Gallery",
            image="test_gallery.jpg"
        )
        self.about = About.objects.create(
            title="Test About",
            content="Test Content"
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.anons, "Test Anons")
        self.assertEqual(self.article.full_text, "Test Full Text")

    def test_slider_image_creation(self):
        self.assertEqual(self.slider_image.title, "Test Slider")
        self.assertEqual(self.slider_image.image, "test_slider.jpg")

    def test_gallery_image_creation(self):
        self.assertEqual(self.gallery_image.title, "Test Gallery")
        self.assertEqual(self.gallery_image.image, "test_gallery.jpg")

    def test_about_creation(self):
        self.assertEqual(self.about.title, "Test About")
        self.assertEqual(self.about.content, "Test Content")
