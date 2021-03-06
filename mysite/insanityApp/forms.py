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
    # image = forms.FileField()
    class Meta:
        model = Item
        fields = ('item_name', 'item_type', 'color', 'code',
                'tot_M', 'tot_L', 'tot_S', 'tot_XS', 'tot_XL')
        # fields = ('item_name', 'item_type', 'color', 'code',
        #     'tot_M', 'tot_L', 'tot_S', 'tot_XS', 'tot_XL', 
        #     'image', )
        item_type = forms.MultipleChoiceField(
            required = False,
            widget = forms.CheckboxSelectMultiple,
            choices = ITEM_TYPE_CHOICES,
        )

class CreateAccessoriesForm(forms.ModelForm):
    tot = forms.IntegerField(min_value = 0, max_value = 100)
    class Meta:
        model = AccessoryItem
        fields = ('item_name', 'item_type', 'color', 'code', 'tot')
        item_type = forms.ChoiceField(
                widget = forms.Select(), 
                choices = ACCESSORY_TYPE_CHOICE,
            )

###############################################

class ClothingFormMan(forms.ModelForm):
    sold = forms.IntegerField(min_value = 0, max_value = 100)
    sold.label = 'N°'
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

class ClothingFormUnisex(forms.ModelForm):
    sold = forms.IntegerField(min_value = 0, max_value = 100)
    sold.label = 'N°'
    class Meta:
        model = Unisex
        fields = ('size','sold', )
        size = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=Size,
        )
        widgests = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class ClothingFormWoman(forms.ModelForm):
    sold = forms.IntegerField(min_value = 0, max_value = 100)
    sold.label = 'N°'
    class Meta:
        model = Woman
        fields = ('size','sold', )
        size = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=Size,
        )
        widgests = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

####################################################################################
class AccessoryFormSold(forms.ModelForm):
    sold = forms.IntegerField(min_value = 0, max_value = 100)
    sold.label = 'N°'
    class Meta:
        model = Accessories
        fields = ('sold', )
        widgests = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


