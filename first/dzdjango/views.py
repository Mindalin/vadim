from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
def index(request):
    posts = Articles.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'dzdjango/index.html', context=context)
def about(request):
    return render(request, 'dzdjango/about.html', {'menu': menu, 'title': 'О сайте'})
def addpage(request):
    return HttpResponse("Добавление статьи")
def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
def archive(request,year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
def show_category(request, cat_id):
    posts = Articles.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'dzdjango/index.html', context=context)