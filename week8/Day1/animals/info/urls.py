from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('family', views.family, name='family'),
    path('animal', views.animal, name='animal'),
]