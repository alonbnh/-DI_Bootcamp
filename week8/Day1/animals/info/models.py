from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=230)


    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=230)
    legs = models.IntegerField(max_length=230)
    weight = models.IntegerField(max_length=230)
    height = models.IntegerField(max_length=230)
    speed = models.IntegerField(max_length=230)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name