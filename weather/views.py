from datetime import datetime
from random import randrange
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from weather.models import WeatherEntity
from weather.repositories import WeatherRepository

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        return render(request, "home.html", {"weathers":weathers})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        wheater = {
            "temperature" : randrange(start=17, stop=40),
            "date": datetime.now()
        }
        repository.insert(wheater)
        return redirect('Weather View')

class ResetAPIView(View):
    def get(self, request):
        # Limpe todos os dados da entidade WeatherEntity
        WeatherEntity.objects.all().delete()
        
        # Retorne uma resposta indicando que a API foi redefinida
        return HttpResponse("API resetada com sucesso!")
