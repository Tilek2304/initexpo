from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    anons = models.TextField()
    full_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='teacher_photos/', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=255, default='Имя')  # Добавлено значение по умолчанию
    last_name = models.CharField(max_length=255, default='Фамилия')  # Добавлено значение по умолчанию
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.address
