from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from .models import Sellers, Buyers, Directory
from .forms import SellersForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render


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

