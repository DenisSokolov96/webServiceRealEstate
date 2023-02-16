from .models import Sellers, Buyers
from django.forms import ModelForm, TextInput


class SellersForm(ModelForm):
    class Meta:
        model = Sellers
        fields = ['fio', 'phone', 'id_district', 'number_floors', 'number_sell_floor', 'area', 'price']
        widgets = {
            'fio': TextInput(attrs={
                 'table-buyers': 'table-buyers',
                 'placeholder': 'ФИО'
            }),
            'phone': TextInput(attrs={
                'table-buyers': 'table-buyers',
                 'placeholder': 'Номер телефона'
            }),
            'id_district': TextInput(attrs={
                'table-buyers': 'table-buyers',
                'placeholder': 'Выберите район'
            }),
            'number_floors': TextInput(attrs={
                'table-buyers': 'table-buyers',
                'placeholder': 'Кол-во этажей в доме'
            }),
            'number_sell_floor': TextInput(attrs={
                'table-buyers': 'table-buyers',
                'placeholder': '№ Этажа'
            }),
            'area': TextInput(attrs={
                'table-buyers': 'table-buyers',
                'placeholder': 'Укажите площадь в м²'
            }),
            'price': TextInput(attrs={
                'table-buyers': 'table-buyers',
                'placeholder': 'Укажите цену в млн.р.'
            })
        }
