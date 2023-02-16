from django.urls import path
from . import views

urlpatterns = [
    path('', views.head, name='head-page'),
    path('sellers', views.get_sellers, name='sellers-page'),
    path('buyers', views.get_buyers, name='buyers-page'),
    path('add_apartment', views.add_apartment, name='add-apartment-page')
]
