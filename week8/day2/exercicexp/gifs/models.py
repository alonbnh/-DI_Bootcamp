from django.db import models
import datetime

class Gif_Model(models.Model):
    title = models.CharField(max_length=230)
    url = models.URLField(max_length=230)
    uploader_name = models.CharField(max_length=230)
    created_at = models.DateField(default=datetime.date.today)
    # def __str__ (self):
    #     return self.title

class Category_Model(models.Model):
    name = models.CharField(max_length=230)
    gifs = models.ManyToManyField(Gif_Model, related_name='categories', blank=True)