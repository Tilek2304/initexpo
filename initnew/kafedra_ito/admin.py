from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.urls import path
from django.template.response import TemplateResponse
from .models import DepartmentITO, TeacherITO, ContactITO, AboutspiITO, AwardITO

class TeacherITOAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = TeacherITO
        fields = '__all__'

class TeacherITOAdmin(admin.ModelAdmin):
    form = TeacherITOAdminForm
    list_display = ('last_name', 'first_name', 'middle_name', 'degree', 'position', 'phone_number', 'email', 'photo', 'is_active')
    fields = ('first_name', 'last_name', 'middle_name', 'degree', 'position', 'phone_number', 'email', 'bio', 'photo', 'is_active')
    list_display_links = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name', 'middle_name', 'degree', 'position', 'phone_number', 'email')
    ordering = ('last_name', 'first_name', 'middle_name', 'degree', 'position', 'phone_number', 'email')
    list_filter = ('is_active',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['first_name'].label = 'Имя'
        form.base_fields['last_name'].label = 'Фамилия'
        form.base_fields['middle_name'].label = 'Отчество'
        form.base_fields['degree'].label = 'Степень'
        form.base_fields['position'].label = 'Должность'
        form.base_fields['phone_number'].label = 'Номер телефона'
        form.base_fields['email'].label = 'Электронная почта'
        form.base_fields['bio'].label = 'Биография'
        form.base_fields['photo'].label = 'Фото'
        form.base_fields['is_active'].label = 'Активный'
        return form

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_head_of_department'] = True
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('head_of_department/', self.admin_site.admin_view(self.head_of_department_view), name='head_of_department'),
            path('documentation/', self.admin_site.admin_view(self.documentation_view), name='documentation'),
        ]
        return custom_urls + urls

    def head_of_department_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            head_of_department=TeacherITO.objects.filter(position='Заведующий кафедрой', is_active=True).first(),
        )
        return TemplateResponse(request, "admin/head_of_department.html", context)

    def documentation_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/documentation.html", context)

class AboutspiITOAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = AboutspiITO
        fields = '__all__'

class AboutspiITOAdmin(admin.ModelAdmin):
    form = AboutspiITOAdminForm

class ContactITOAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = ContactITO
        fields = '__all__'

class ContactITOAdmin(admin.ModelAdmin):
    form = ContactITOAdminForm

admin.site.register(TeacherITO, TeacherITOAdmin)
admin.site.register(ContactITO, ContactITOAdmin)
admin.site.register(AboutspiITO, AboutspiITOAdmin)
admin.site.register(AwardITO)  # Зарегистрировать модель AwardITO
