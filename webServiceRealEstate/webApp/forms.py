from .models import Sellers, Buyers
from django.forms import ModelForm, TextInput


class SellersForm(ModelForm):
    class Meta:
        model = Sellers
        fields = ['fio', 'phone', 'id_district', 'number_floors', 'number_sell_floor', 'area', 'price']
        widgets = {
            'fio': TextInput(attrs={
                 'placeholder': 'ФИО'
            }),
            'phone': TextInput(attrs={
                 'placeholder': 'Номер телефона'
            }),
            'id_district': TextInput(attrs={
                'placeholder': 'Выберите район'
            }),
            'number_floors': TextInput(attrs={
                'placeholder': 'Кол-во этажей в доме'
            }),
            'number_sell_floor': TextInput(attrs={
                'placeholder': '№ Этажа'
            }),
            'area': TextInput(attrs={
                'placeholder': 'Укажите площадь в м²'
            }),
            'price': TextInput(attrs={
                'placeholder': 'Укажите цену в млн.р.'
            })
        }


class BuyersForm(ModelForm):
    class Meta:
        model = Buyers
        fields = ['fio', 'phone', 'id_district', 'area', 'price']
        widgets = {
            'fio': TextInput(attrs={
                 'placeholder': 'ФИО'
            }),
            'phone': TextInput(attrs={
                 'placeholder': 'Номер телефона'
            }),
            'id_district': TextInput(attrs={
                'placeholder': 'Выберите район'
            }),
            'area': TextInput(attrs={
                'placeholder': 'Укажите площадь в м²'
            }),
            'price': TextInput(attrs={
                'placeholder': 'Укажите цену в млн.р.'
            })
        }
