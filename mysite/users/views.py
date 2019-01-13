from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.generic.list import ListView
from users.models import Film

#from django.utils import timezone

class FilmsList(ListView):
    model = Film#(name='kris',genre='yulis',issue='1998',director='ya',description='ou')
    #model.save()
    #model.get_deferred_fields()

def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        alldata = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        for i in alldata['orders']:
            if i['id']==id:
                data = {
                    'order': {
                        'id': id,
                        'title': i['title']
                    }
                }
        return render(request, 'order.html', data)
        