from django.contrib import admin
from .models import Articles, Comment
from django.utils.html import format_html

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'image_tag')  # Добавить поле автор
    search_fields = ('title', 'author')  # Добавить поле автор для поиска
    list_filter = ('date', 'author')  # Добавить поле автор для фильтрации

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />'.format(obj.image.url))
        return '-'
    image_tag.short_description = 'Изображение'

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment)  # Зарегистрировать модель Comment
