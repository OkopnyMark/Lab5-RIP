from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.generic import ListView
from users.models import Film

class FilmsList(ListView):
    def get(self):
        model = Film
        return model.get_deferred_fields(self)
model = Film
FilmsList.get(model)