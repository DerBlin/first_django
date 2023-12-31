from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    dir_list = os.listdir(path='C:\\Users\\ewbli\\OneDrive\\Рабочий стол\\DJANGO_HW\\dj-homeworks\\first-project\\first_project')
    done_list = str(dir_list).split()
    msg = f'В основной директории проекта {len(done_list)} файлов: {done_list}'
    return HttpResponse(msg)
