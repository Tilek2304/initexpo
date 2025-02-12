from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class DepartmentITO(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)  # Добавленное поле

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра ИТО'
        verbose_name_plural = 'Кафедры ИТО'

class TeacherITO(models.Model):
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
        verbose_name = 'Преподаватель ИТО'
        verbose_name_plural = 'Преподаватели ИТО'

class AboutITO(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class ContactITO(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт ИТО'
        verbose_name_plural = 'Контакты ИТО'

class AboutspiITO(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='aboutspi_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О кафедре ИТО'
        verbose_name_plural = 'О кафедре ИТО'

class AwardITO(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='awards/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Награда ИТО"
        verbose_name_plural = "Награды ИТО"

class ItoDocSection(models.Model):
    name = models.CharField(max_length=255)
    document_count = models.IntegerField()
