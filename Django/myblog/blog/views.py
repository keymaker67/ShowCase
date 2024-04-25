from django.shortcuts import render,redirect
from django.contrib import messages
# from django.http import HttpResponse

from .models import ArticleModel
from .forms import CreateArticle


def home(request):
    articles = ArticleModel.objects.all().order_by("-created_date")
    return render(request, "main/home.html", {"articles": articles})


def about(request):
    return render(request, "main/about.html")


def article(request, slug):
    the_article = ArticleModel.objects.get(slug=slug)
    return render(request, "main/article.html", {"the_article": the_article})


def create_article(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login required!')
        return redirect('blog:home')
    if request.method == "POST":
        create_article_form = CreateArticle(request.POST, request.FILES)
        if create_article_form.is_valid():
            save_article_form = create_article_form.save(commit=False)
            save_article_form.author = request.user
            save_article_form.save()
            return redirect('blog:home')
    else:
        create_article_form = CreateArticle()
    return render(request, 'main/create_article.html', {"create_article_form": create_article_form})
