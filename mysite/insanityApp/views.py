from django.shortcuts import render
from django.forms import inlineformset_factory
from django.http import HttpResponse

from .models import *
from .forms import *

import datetime

# Create your views here.

def home(request):
    return render(request, 'insanityApp/home.html')

def create(request):
    return render(request, 'insanityApp/create.html', {})

def new(request):
    context = {}
    items = Item.objects.all()

    if request.method == 'POST':
        form = CreateItemForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            item = form.save(commit=False)
            tot_XS = form.cleaned_data.get('tot_XS')
            tot_S = form.cleaned_data.get('tot_S')
            tot_M = form.cleaned_data.get('tot_M')
            tot_L = form.cleaned_data.get('tot_L')
            tot_XL = form.cleaned_data.get('tot_XL')
            item.remaining_XS = tot_XS
            item.remaining_S = tot_S
            item.remaining_M = tot_M
            item.remaining_L = tot_L
            item.remaining_XL = tot_XL
            item.save()
    else:
        form = CreateItemForm()

    return render(request, 'insanityApp/new.html', {'form':form, 'items':items})


def report(request):
    context = {}
    items = Item.objects.all()
    return render(request, 'insanityApp/report.html', {'items':items})

def man(request):
    context={}
    items = Item.objects.all()
    items_man = Man.objects.all()

    a = []
    for k in request.POST:
        a.append(k)

    form = ClothingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            clothing = form.save(commit=False)
            now = datetime.datetime.now()
            items_man.date = now
            clothing.save()

            item_size = form.cleaned_data.get('size')
            print('item size =', item_size )
            print('item sold =', form.cleaned_data.get('sold') )

            if a != []:
                # save the item's code
                print('code =', a[3])
                last_item = items_man.last()
                last_item.code = a[3]
                last_item.save()

                # save the remaining size of this item 
                # list_size = {'remaining_XS' : 'XS', 
                #             'remaining_S' : 'S',
                #             'remaining_M' : 'M',
                #             'remaining_L' : 'L',
                #             'remaining_XL' : 'XL'
                #             }
                
                for item in items:
                    if item.code == a[3]:
                        if item_size == 'XS':
                            if last_item.sold <= item.remaining_XS:
                                item.remaining_XS = item.remaining_XS - last_item.sold
                                print('XS rimanenti =',  item.remaining_XS)
                                item.save()
                            elif item.remaining_XS == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'S':
                            if last_item.sold <= item.remaining_S:
                                item.remaining_S = item.remaining_S - last_item.sold
                                print('S rimanenti =',  item.remaining_S)
                                item.save()
                            elif item.remaining_S == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'M':
                            if last_item.sold <= item.remaining_M:
                                item.remaining_M = item.remaining_M - last_item.sold
                                print('M rimanenti =',  item.remaining_M)
                                item.save()
                            elif item.remaining_M == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'L':
                            if last_item.sold <= item.remaining_L:
                                item.remaining_L = item.remaining_L - last_item.sold
                                print('L rimanenti =',  item.remaining_L)
                                item.save()
                            elif item.remaining_L == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'XL':
                            if last_item.sold <= item.remaining_XL:
                                item.remaining_XL = item.remaining_XL - last_item.sold
                                print('XL rimanenti =',  item.remaining_XL)
                                item.save()
                            elif item.remaining_XL == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                                
                #         elif item_size == 'S':
                #             last_item.remaining_S = item.tot_S - last_item.sold
                #             print('S rimanenti =',  last_item.remaining_S)
                #             last_item.save()
                #         elif item_size == 'M':
                #             last_item.remaining_M = item.tot_M - last_item.sold
                #             print('M rimanenti =',  last_item.remaining_M)
                #             last_item.save()
                #         elif item_size == 'L':
                #             last_item.remaining_L = item.tot_L - last_item.sold
                #             print('L rimanenti =',  last_item.remaining_L)
                #             last_item.save()
                #         elif item_size == 'XL':
                #             last_item.remaining_L = item.tot_XL - last_item.sold
                #             print('XL rimanenti =',  last_item.remaining_XL)
                #             last_item.save()
                #         else:
                #             print('Size Error')
    else:
        form = ClothingForm()
        
    context['form'] = form
    context['items'] = items
    return render(request, 'insanityApp/man.html', context)

def woman(request):
    context={}
    items = Item.objects.all()
    items_woman = Woman.objects.all()

    a = []
    for k in request.POST:
        a.append(k)

    form = ClothingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            clothing = form.save(commit=False)
            now = datetime.datetime.now()
            items_woman.date = now
            clothing.save()

            item_size = form.cleaned_data.get('size')
            print('item size =', item_size )
            print('item sold =', form.cleaned_data.get('sold') )

            if a != []:
                # save the item's code
                print('code =', a[3])
                last_item = items_woman.last()
                last_item.code = a[3]
                last_item.save()

                # save the remaining size of this item 
                # list_size = {'remaining_XS' : 'XS', 
                #             'remaining_S' : 'S',
                #             'remaining_M' : 'M',
                #             'remaining_L' : 'L',
                #             'remaining_XL' : 'XL'
                #             }
                
                for item in items:
                    if item.code == a[3]:
                        if item_size == 'XS':
                            if last_item.sold <= item.remaining_XS:
                                item.remaining_XS = item.remaining_XS - last_item.sold
                                print('XS rimanenti =',  item.remaining_XS)
                                item.save()
                            elif item.remaining_XS == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'S':
                            if last_item.sold <= item.remaining_S:
                                item.remaining_S = item.remaining_S - last_item.sold
                                print('S rimanenti =',  item.remaining_S)
                                item.save()
                            elif item.remaining_S == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'M':
                            if last_item.sold <= item.remaining_M:
                                item.remaining_M = item.remaining_M - last_item.sold
                                print('M rimanenti =',  item.remaining_M)
                                item.save()
                            elif item.remaining_M == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'L':
                            if last_item.sold <= item.remaining_L:
                                item.remaining_L = item.remaining_L - last_item.sold
                                print('L rimanenti =',  item.remaining_L)
                                item.save()
                            elif item.remaining_L == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        elif item_size == 'XL':
                            if last_item.sold <= item.remaining_XL:
                                item.remaining_XL = item.remaining_XL - last_item.sold
                                print('XL rimanenti =',  item.remaining_XL)
                                item.save()
                            elif item.remaining_XL == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                # return render(request, 'insanityApp/man.html', context)
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                                
                #         elif item_size == 'S':
                #             last_item.remaining_S = item.tot_S - last_item.sold
                #             print('S rimanenti =',  last_item.remaining_S)
                #             last_item.save()
                #         elif item_size == 'M':
                #             last_item.remaining_M = item.tot_M - last_item.sold
                #             print('M rimanenti =',  last_item.remaining_M)
                #             last_item.save()
                #         elif item_size == 'L':
                #             last_item.remaining_L = item.tot_L - last_item.sold
                #             print('L rimanenti =',  last_item.remaining_L)
                #             last_item.save()
                #         elif item_size == 'XL':
                #             last_item.remaining_L = item.tot_XL - last_item.sold
                #             print('XL rimanenti =',  last_item.remaining_XL)
                #             last_item.save()
                #         else:
                #             print('Size Error')
    else:
        form = ClothingForm()
        
    context['form'] = form
    context['items'] = items
    return render(request, 'insanityApp/woman.html', context)

def accessories(request):
    return render(request, 'insanityApp/accessories.html', {})

def bracelets(request):
    return render(request, 'insanityApp/bracelets.html', {})


