"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from main.views import test_page, html_page, cars_list, cars_details, hello, sum, convertor_format, demo_html, pagi, recept, create_car, list_car, create_person, list_person
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'
    def to_python(self, value: str):
        return datetime.strptime(value, self.format)
    def to_url(self, value: datetime):
        return datetime.strftime(self.format)
    
register_converter(DateConverter, 'date')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_page),
    path('html/', html_page),
    path('cars/', cars_list, name='list'),
    path('cars/<int:car_id>/', cars_details, name='details'),
    path('hello/', hello),
    path('demo_html/', demo_html),
    path('sum/<int:op1>/<int:op2>/', sum),
    path('convertor_format/<int:id>/<date:dt>/', convertor_format),
    path('pagi/', pagi),
    path('recept/<str:opt1>/', recept),
    path('new_car/', create_car),
    path('list_car/', list_car),
    path('new_person/', create_person),
    path('list_person/', list_person),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)