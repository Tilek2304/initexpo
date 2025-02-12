from django import forms
from .models import Articles, Comment, ArticleImage

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'image', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'anons': forms.TextInput(attrs={'class': 'form-control'}),
            'full_text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class ArticleImageForm(forms.Form):
    images = forms.FileField(widget=MultiFileInput(attrs={'multiple': True, 'class': 'form-control'}), required=False)
