from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, shop, *args, **kwargs): # NOTE: 특정 shop의 상품만 가져오는 queryset
        super().__init__(*args, **kwargs)
        self.fields['item_set'].queryset = self.fields['item_set'].queryset.filter(shop=shop)

    class Meta:
        model = Order
        fields = ['item_set']
