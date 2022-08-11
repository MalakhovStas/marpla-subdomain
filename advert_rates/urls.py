from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdvertRates.as_view(), name='advert_rates'),
    path('api/', views.AdvertRatesJson.as_view(), name='advert_rates_json')
]