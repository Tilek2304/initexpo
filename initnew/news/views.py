from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from .models import Articles, Comment, ArticleImage
from .forms import ArticlesForm, CommentForm, ArticleImageForm
from django.core.paginator import Paginator
from django.utils.translation import gettext as _

def news_home(request):
    news_list = Articles.objects.all().order_by('-date')
    paginator = Paginator(news_list, 20)  # Пагинация по 20 новостей на странице

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    return render(request, 'news/news_home.html', {"news": news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail_view.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404(_("Article not found."))
        obj.views += 1  # Увеличить количество просмотров
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_images'] = self.object.images.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        image_form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return redirect('news_detail_view', pk=self.object.pk)
        if image_form.is_valid():
            for file in request.FILES.getlist('images'):
                ArticleImage.objects.create(article=self.object, image=file)
            return redirect('news_detail_view', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

def create_news(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        image_form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            article = form.save()
            for file in request.FILES.getlist('images'):
                ArticleImage.objects.create(article=article, image=file)
            return redirect('news_home')
    else:
        form = ArticlesForm()
        image_form = ArticleImageForm()
    return render(request, 'news/create_news.html', {'form': form, 'image_form': image_form})

def edit_news(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        image_form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            form.save()
            for file in request.FILES.getlist('images'):
                ArticleImage.objects.create(article=article, image=file)
            return redirect('news_detail_view', pk=article.pk)
    else:
        form = ArticlesForm(instance=article)
        image_form = ArticleImageForm()
    return render(request, 'news/edit_news.html', {'form': form, 'image_form': image_form})

def upload_images(request):
    if request.method == 'POST':
        form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            for image in images:
                ArticleImage.objects.create(image=image)
            return redirect('success_url')
    else:
        form = ArticleImageForm()
    return render(request, 'upload.html', {'form': form})
