from django.urls import path
from . import views

urlpatterns = [
    path('', views.head, name='head-page'),
    path('sellers', views.get_sellers, name='sellers-page'),
    path('buyers', views.get_buyers, name='buyers-page'),

    path('add_apartment', views.add_apartment, name='add-apartment-page'),
    path('add_buyer', views.add_buyer, name='add-buyer-page'),

    path('buyers/<int:pk>', views.buyesDetail, name='buyer-detail'),
    path('buyers/<int:pk>/update', views.updateBuyers, name='buyer-update'),
    path('buyers/<int:pk>/del_buyer', views.DelBuyer.as_view(), name='del-buyer'),

    path('sellers/<int:pk>', views.sellersDetail, name='seller-detail'),
    path('sellers/<int:pk>/update', views.updateSellers, name='seller-update'),
    path('sellers/<int:pk>/del_seller', views.DelSeller.as_view(), name='del-seller')
]
