from django.db import models
from datetime import datetime

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

class PDFDocument(models.Model):
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=2025)
    file = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # Новое поле
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Новое поле

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "PDF документ"
        verbose_name_plural = "PDF документы"
