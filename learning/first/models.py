from django.db import models

# Create your models here.
class Students(models.Model):
    # id=models.AutoField()

    name=models.CharField(max_length=100)
    age=models.IntegerField()
    location=models.TextField(null=True, blank=True)
    image=models.ImageField()

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
# read
    def __str__(self) -> str:
        return self.car_name