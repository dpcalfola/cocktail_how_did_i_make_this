from django.urls import path
from . import views

app_name = 'market_price'

urlpatterns = [
    path('', views.price_table, name='price_table'),
]
