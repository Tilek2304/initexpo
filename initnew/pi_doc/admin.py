from django.contrib import admin
from .models import Document, Section, PDFDocument

# Register your models here.


admin.site.register(Section)
admin.site.register(PDFDocument)
