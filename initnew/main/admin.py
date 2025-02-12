from django.contrib import admin
from .models import SliderImage, GalleryImage, Articles, About, Department, Teacher, Contact

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('is_active',)
    verbose_name = 'Слайдер'
    verbose_name_plural = 'Слайдеры'

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('is_active',)
    verbose_name = 'Галерея'
    verbose_name_plural = 'Галереи'

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'views_count')
    search_fields = ('title', 'anons', 'full_text')
    list_filter = ('date',)
    readonly_fields = ('views_count',)
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'

class AboutAdmin(admin.ModelAdmin):  # Обновлено с AboutUsAdmin на AboutAdmin
    list_display = ('title',)
    search_fields = ('title', 'content')
    verbose_name = 'О нас'
    verbose_name_plural = 'О нас'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = 'Отдел'
    verbose_name_plural = 'Отделы'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'degree', 'position', 'phone_number', 'email', 'photo')
    search_fields = ('last_name', 'first_name', 'middle_name', 'degree', 'position', 'phone_number', 'email')
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    verbose_name = 'Контакт'
    verbose_name_plural = 'Контакты'

admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(About, AboutAdmin)  # Обновлено с AboutUs на About




