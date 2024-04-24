from django.shortcuts import render
from django.core.paginator import Paginator 
from django.http import HttpResponse, Http404

from main.models import Car
from datetime import datetime

def test_page(requests):
    return HttpResponse('Привет!')


def html_page(requests):
    
    content = """

"""
    return HttpResponse(content)


def cars_list(requests):
    cars = Car.objects.all()
    return render(requests, template_name='list.html', context= {'cars': cars})


def cars_details(requests, car_id):
    try:
        car = Car.objects.get(id = car_id)
        return render(requests, template_name='details.html', context= {'car': car})
    except Car.DoesNotExist:
        raise Http404('Car not found')
    

def hello(requests):
    # name = requests.GET['name'] # Если такого ключа в запросе не будет, то выпадет ошибка
    # age = requests.GET['age'] # Если такого ключа в запросе не будет, то выпадет ошибка

    name = requests.GET.get('name') # безопасно достать ключ, если он имеется
    age = requests.GET.get('age', 'Дефолтное значение') # безопасно достать ключ, если он имеется
    return HttpResponse(f'Привет {name}, тебе {age} года')


def sum(requests, op1, op2):
    result = op1 + op2
    return HttpResponse(f'Sum = {result}')


def convertor_format(requests, id: int, dt: datetime):
    return HttpResponse(f'{id}  {dt}')


def demo_html(requests):
    context = {
        'test': 5,
        'data': [1 ,5, 7, 88, 99],
        'val': 'hello'
        }
    return render(requests, 'demo.html', context)

CONTENT = [str(i) for i in range(10000)]

def pagi(requests):
    page_number = int(requests.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
        }
    return render(requests, 'pagi.html', context)