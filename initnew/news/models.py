from django.db import models
from ckeditor.fields import RichTextField

class Articles(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = RichTextField('Статья')  # Использование Rich Text Editor
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='news_images/', blank=True, null=True)
    author = models.CharField('Автор', max_length=100, default='Баян Токтомуш уулу')  # Добавить значение по умолчанию
    views = models.PositiveIntegerField('Количество просмотров', default=0)  # Добавить поле для количества просмотров

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class ArticleImage(models.Model):
    article = models.ForeignKey(Articles, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='news_images/')

    def __str__(self):
        return f"Изображение для {self.article.title}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Comment(models.Model):
    article = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField('Автор', max_length=100)
    text = models.TextField('Комментарий')
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
