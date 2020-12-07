from django.forms import ModelForm

from .models import *


class CustomerProfileForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


