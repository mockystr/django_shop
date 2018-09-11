from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Quantity'))
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput(attrs={'class': 'btn btn-info'}))

    # def __init__(self, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'btn btn-info'
