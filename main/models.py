from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'