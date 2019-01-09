from django import forms
from .models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.core.files.storage import default_storage
from django.http import JsonResponse

###############################################
class CreateItemForm(forms.ModelForm):
    tot_XS= forms.IntegerField(min_value = 0, max_value = 100)
    tot_S= forms.IntegerField(min_value = 0, max_value = 100)
    tot_M= forms.IntegerField(min_value = 0, max_value = 100)
    tot_L= forms.IntegerField(min_value = 0, max_value = 100)
    tot_XL= forms.IntegerField(min_value = 0, max_value = 100)
    image = forms.FileField()
    class Meta:
        model = Item
        fields = ('item_name', 'item_type', 'color', 'code',
                'tot_M', 'tot_L', 'tot_S', 'tot_XS', 'tot_XL', 
                'image', )
        item_type = forms.MultipleChoiceField(
            required = False,
            widget = forms.CheckboxSelectMultiple,
            choices = ITEM_TYPE_CHOICES,
        )


###############################################

class ClothingForm(forms.ModelForm):
    sold = forms.IntegerField(min_value = 0, max_value = 100)
    class Meta:
        model = Man
        fields = ('size','sold', )
        size = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=Size,
        )
        widgests = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
