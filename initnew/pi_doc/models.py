from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Добавить описание

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление докуменирования"
        verbose_name_plural = "Направление докуменирования"

class PDFDocument(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    year = models.PositiveIntegerField(default=2025)  # Временный дефолт
    description = models.TextField(blank=True, null=True)  # Добавить описание

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "PDF Документ"
        verbose_name_plural = "PDF Документы"
