from django.contrib import admin

# Register your models here.

# python manage.py createsuperuser нужно чтобы создать супераользователя и зайти в админ панель

from main.models import Car, Car1, Person

admin.site.register(Car)

@admin.register(Car1) # при помощи декоратора регистрируем для какой модели данный класс будет являться описателем
class Car1_admin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']

@admin.register(Person) # при помощи декоратора регистрируем для какой модели данный класс будет являться описателем
class Person_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    # list_filter = ['brand', 'model']