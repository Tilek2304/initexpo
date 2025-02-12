from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="Unknown")
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = RichTextField()
    photo = models.ImageField(upload_to='teachers_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Aboutspi(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='aboutspi_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О кафедре'
        verbose_name_plural = 'О кафедре'

class Award(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='awards/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
