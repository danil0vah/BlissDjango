from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

database = [{'foreign_key' : 1,'tour_name' : 'Туры по горам Тянь-Шаня'},
        {'foreign_key' : 2,'tour_name' : 'Туры по Иссык-Кулю'},
        {'foreign_key' : 3,'tour_name' : 'Туры по Чуйской долине'},
        {'foreign_key' : 4,'tour_name' : 'Туры по Бишкеку'}]


def index(request): 
    data = {'title': 'Бliss Tours - Туры по Кыргызстану',
            'tours': database}
    return render(request, 'landing/index.html', context = data)


def tours(HttpRequest, tour_id): 
    return HttpResponse(f'<h1>Горящие туры по Кыргызстану</h1><p>ID: {tour_id}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена')