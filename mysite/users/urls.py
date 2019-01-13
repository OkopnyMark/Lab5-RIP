from django.urls import path
from . import views
from users.views import FilmsList

urlpatterns = [
    path('', views.index),
    path('orders/<int:id>', views.OrderView.as_view(), name='order_url'),
    path('orders/', views.OrdersView.as_view(), name='order_url'),
    path('cinema/films/', FilmsList.as_view(), name = 'film-list'),
]