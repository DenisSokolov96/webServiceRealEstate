from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView, UpdateView

from .models import Sellers, Buyers, Directory
from .forms import SellersForm, BuyersForm
from django.core.paginator import Paginator
from django.shortcuts import render


# классы добавления / вывода / удаления покупателей(заказчиков) квартир
class BuyesDetail(DetailView):
    model = Buyers
    template_name = 'webApp/details_buyers.html'
    context_object_name = 'buyer'


class DelBuyer(DeleteView):
    model = Buyers
    success_url = '/buyers'
    template_name = 'webApp/del_buyers.html'
    context_object_name = 'buyer'


class BuyersUpdateView(UpdateView):
    model = Buyers
    template_name = 'webApp/add_buyer.html'
    success_url = '/buyers'
    fields = ['fio', 'phone', 'id_district', 'area', 'price']


# классы добавления / вывода / удаления продавцов
class SellersDetail(DetailView):
    model = Sellers
    template_name = 'webApp/details_sellers.html'
    context_object_name = 'sellers'


class DelSeller(DeleteView):
    model = Sellers
    success_url = '/sellers'
    template_name = 'webApp/del_sellers.html'
    context_object_name = 'seller'


class SellersUpdateView(UpdateView):
    model = Sellers
    template_name = 'webApp/add_apartment.html'
    success_url = '/sellers'
    fields = ['fio', 'phone', 'id_district', 'number_floors', 'number_sell_floor', 'area', 'price']


def head(request):
    num_apartments = Sellers.objects.all().count()
    num_buyers = Buyers.objects.all().count()

    # это можно исправить одним запросом
    districts = Directory.objects.all()
    rayon = {}
    for el in districts:
        rayon[el.name_district] = Sellers.objects.filter(id_district=el.id).count()
    num_district = len(districts)
    context = {
        'num_apartments': num_apartments,
        'num_buyers': num_buyers,
        'num_district': num_district,
        'area': rayon
    }
    return render(request, 'webApp/index.html', context)


def get_sellers(request):
    sellers = Sellers.objects.order_by('-id')
    # подмена id района - названием
    for seller in sellers:
        seller.id_district = Directory.objects.filter(id=seller.id_district)[0].name_district
    paginator = Paginator(sellers, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webApp/sellers.html', {'paginator': paginator, 'page_obj': page_obj, 'title': 'Продавцы'})


def get_buyers(request):
    buyers = Buyers.objects.order_by('-id')
    # подмена id района - названием
    for buyer in buyers:
        buyer.id_district = Directory.objects.filter(id=buyer.id_district)[0].name_district
    paginator = Paginator(buyers, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webApp/buyers.html', {'paginator': paginator, 'page_obj': page_obj, 'title': 'Покупатели'})


def add_apartment(request):
    error = ''
    if request.method == 'POST':
        form = SellersForm(request.POST)
        # подмена названия района на id
        # area = form.cleaned_data['id_district']
        # form.cleaned_data['id_district'] = Directory.objects.filter(name_district=area)[0].name_district
        if form.is_valid():
            form.save()
            return redirect('sellers-page')
        else:
            error = 'Форма была неверной!'

    form = SellersForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'webApp/add_apartment.html', context)


def add_buyer(request):
    error = ''
    if request.method == 'POST':
        form = BuyersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyers-page')
        else:
            error = 'Форма была неверной!'

    form = BuyersForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'webApp/add_buyer.html', context)
