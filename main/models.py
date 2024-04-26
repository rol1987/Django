from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'
    

class Car1(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.brand} {self.model} {self.color}'
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car1, on_delete = models.CASCADE, related_name='owners') # on_delete = models.CASCADE - что сделать, если машина будет удалена. Человек удалится, если будет удалена запись об автомобиле

    def __str__(self):
        return f'{self.name} {self.car}'