from django.shortcuts import render
from django.core.paginator import Paginator 
from django.http import HttpResponse, Http404

from main.models import Car, Car1, Person
from datetime import datetime
import random

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


def demo_html(requests):
    context = {
        'test': 5,
        'data': [1 ,5, 7, 88, 99],
        'val': 'hello'
        }
    return render(requests, 'demo.html', context)


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recept(requests, opt1):
    # recipe = requests.GET.get('recipe')
    recipe = opt1
    servings = int(requests.GET.get('servings', 1))
    context = {
        # 'recipe': DATA[recipe]
        'recipe': [f'{key}: {str(value*servings)}' for key, value in DATA[recipe].items()]
            }
    print(context)
    return render(requests, 'index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def create_car(requests):
    car = Car1(
        brand = random.choice(['B1', 'B2', 'B3']),
        model = random.choice(['M1', 'M2', 'M3']),
        color = random.choice(['C1', 'C2', 'C3']),
        )
    car.save()
    return HttpResponse(f'Все получилось! новая машина {car.brand} {car.model}')

def list_car(requests):
    # car_objects = Car1.objects.all() # получаем все объекты из базы данных
    # car_objects = Car1.objects.filter(brand = 'B1') # получаем объекты по критериям
    # car_objects = Car1.objects.filter(brand__contains = '2') # получаем объекты по критериям: brand содержит цифру 2
    car_objects = Car1.objects.filter(brand__startswith = 'B') # получаем объекты по критериям: brand начинается с подстроки B
    cars = [f'{c.id}: {c.brand} {c.model}: {c.color} / {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car1.objects.all()
    for car in cars:
        # Person(name='P', car = car).save() #Первый способ записи в базу
        Person.objects.create(name='Q', car = car) #Второй способ записи в базу
    
    return HttpResponse('Все получилось!')
 

def list_person(requests):
    person_objects = Person.objects.all() # получаем объекты по критериям: brand начинается с подстроки B
    person = [f'{p.id}: {p.name} {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(person))