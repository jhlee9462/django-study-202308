from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleModelForm
from django.urls import reverse


# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self, queryset=Article.objects.filter(id__gt=1)):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    queryset = Article.objects.all()
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self, queryset=Article.objects.all()):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self, queryset=Article.objects.filter(id__gt=1)):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')
