from django.shortcuts import render
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpRequest

from .models import *
from .forms import *

import datetime

# Create your views here.

def home(request):
    return render(request, 'insanityApp/home.html')

def create(request):
    return render(request, 'insanityApp/create.html', {})

def new_accessories(request):
    context={}
    items = AccessoryItem.objects.all()

    form = CreateAccessoriesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            item = form.save(commit=False)
            tot = form.cleaned_data.get('tot')
            item.tot_remaining = tot
            item.save()
        else:
            form = CreateAccessoriesForm()

    context['form'] = form
    return render(request, 'insanityApp/settings/new_accessories.html', context)

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

    return render(request, 'insanityApp/settings/new.html', {'form':form, 'items':items})


def report(request):
    context = {}
    items = Item.objects.all()
    accessories = AccessoryItem.objects.all()
    return render(request, 'insanityApp/settings/report.html', {'items':items , 'accessories': accessories})

def man(request):
    context={}
    items = Item.objects.all()
    items_man = Man.objects.all()
    items_unisex = Unisex.objects.all()
    form_unisex = ClothingFormUnisex(request.POST)
    form_man = ClothingFormMan(request.POST)

    a = []
    for k in request.POST:
        a.append(k)

    if a != []:
        print(a[3].split(','))
        b = a[3].split(',')
        print('b[0] =', b[0])
        print('b[1] =', b[1])
        print('b[2] =', b[2])


        if b[0] == 'Unisex':
            if request.method == 'POST':
                if form_unisex.is_valid():
                    clothing = form_unisex.save(commit=False)
                    now = datetime.datetime.now()
                    items_unisex.date = now
                    clothing.save()
            else:
                form_unisex = ClothingFormUnisex()

            last_item = items_unisex.last()
            last_item.code = b[1]
            activity = b[2]
            last_item.activity = activity
            last_item.save()

            item_size = form_unisex.cleaned_data.get('size')
            print('item size =', item_size )
            print('item sold =', form_unisex.cleaned_data.get('sold') )

            # save the remaining size of this item
            for item in items:
                if item.code == b[1]:
                    if item_size == 'XS':
                        if (b[2] == 'Venduto') :
                            check_XS(item, last_item)
                            # return render(request, 'insanityApp/home.html', context)
                        else: #'Aggiungi'
                            item.tot_XS = item.tot_XS + last_item.sold
                            item.remaining_XS = item.remaining_XS + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'S':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_S:
                                item.remaining_S = item.remaining_S - last_item.sold
                                print('S rimanenti =',  item.remaining_S)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_S == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_S = item.tot_S + last_item.sold
                            item.remaining_S = item.remaining_S + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'M':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_M:
                                item.remaining_M = item.remaining_M - last_item.sold
                                print('M rimanenti =',  item.remaining_M)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_M == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_M = item.tot_M + last_item.sold
                            item.remaining_M = item.remaining_M + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'L':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_L:
                                item.remaining_L = item.remaining_L - last_item.sold
                                print('L rimanenti =',  item.remaining_L)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_L == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_L = item.tot_L + last_item.sold
                            item.remaining_L = item.remaining_L + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'XL':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_XL:
                                item.remaining_XL = item.remaining_XL - last_item.sold
                                print('XL rimanenti =',  item.remaining_XL)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_XL == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_XL = item.tot_XL + last_item.sold
                            item.remaining_XL = item.remaining_XL + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)

        elif b[0] == 'Man':
            if request.method == 'POST':
                if form_man.is_valid():
                    clothing = form_man.save(commit=False)
                    now = datetime.datetime.now()
                    items_man.date = now
                    clothing.save()
            else:
                form_man = ClothingFormMan()

            last_item = items_man.last()
            last_item.code = b[1]
            activity = b[2]
            last_item.activity = activity
            last_item.save()

            item_size = form_man.cleaned_data.get('size')
            print('item size =', item_size )
            print('item sold =', form_man.cleaned_data.get('sold') )

            # save the remaining size of this item
            for item in items:
                if item.code == b[1]:
                    if item_size == 'XS':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_XS:
                                item.remaining_XS = item.remaining_XS - last_item.sold
                                print('XS rimanenti =',  item.remaining_XS)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_XS == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_XS = item.tot_XS + last_item.sold
                            item.remaining_XS = item.remaining_XS + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'S':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_S:
                                item.remaining_S = item.remaining_S - last_item.sold
                                print('S rimanenti =',  item.remaining_S)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_S == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_S = item.tot_S + last_item.sold
                            item.remaining_S = item.remaining_S + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'M':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_M:
                                item.remaining_M = item.remaining_M - last_item.sold
                                print('M rimanenti =',  item.remaining_M)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_M == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_M = item.tot_M + last_item.sold
                            item.remaining_M = item.remaining_M + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'L':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_L:
                                item.remaining_L = item.remaining_L - last_item.sold
                                print('L rimanenti =',  item.remaining_L)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_L == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_L = item.tot_L + last_item.sold
                            item.remaining_L = item.remaining_L + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)
                    elif item_size == 'XL':
                        if (b[2] == 'Venduto') :
                            if last_item.sold <= item.remaining_XL:
                                item.remaining_XL = item.remaining_XL - last_item.sold
                                print('XL rimanenti =',  item.remaining_XL)
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                            elif item.remaining_XL == 0:
                                print('non ne hai più')
                                return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                            else:
                                return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                        else: #'Aggiungi'
                            item.tot_XL = item.tot_XL + last_item.sold
                            item.remaining_XL = item.remaining_XL + last_item.sold
                            item.save()
                            return render(request, 'insanityApp/home.html', context)

    context['items'] = items
    context['form_unisex'] = form_unisex
    context['form_man'] = form_man
    return render(request, 'insanityApp/man.html', context)


def woman(request):
    context={}
    items = Item.objects.all()
    items_woman = Woman.objects.all()
    items_unisex = Unisex.objects.all()
    form_unisex = ClothingFormUnisex(request.POST)
    form_woman = ClothingFormWoman(request.POST)

    a = []
    for k in request.POST:
        a.append(k)

    if a != []:
        print(a[3].split(','))
        b = a[3].split(',')
        print('b[0] =', b[0])
        print('b[1] =', b[1])


        if b[0] == 'Unisex':
            if request.method == 'POST':
                if form_unisex.is_valid():
                    clothing = form_unisex.save(commit=False)
                    now = datetime.datetime.now()
                    items_unisex.date = now
                    clothing.save()


                last_item = items_unisex.last()
                last_item.code = b[1]
                activity = b[2]
                last_item.activity = activity
                last_item.save()

                item_size = form_unisex.cleaned_data.get('size')
                print('item size =', item_size )
                print('item sold =', form_unisex.cleaned_data.get('sold') )

                # save the remaining size of this item
                for item in items:
                    if item.code == b[1]:
                        if item_size == 'XS':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_XS:
                                    item.remaining_XS = item.remaining_XS - last_item.sold
                                    print('XS rimanenti =',  item.remaining_XS)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_XS == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_XS = item.tot_XS + last_item.sold
                                item.remaining_XS = item.remaining_XS + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'S':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_S:
                                    item.remaining_S = item.remaining_S - last_item.sold
                                    print('S rimanenti =',  item.remaining_S)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_S == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_S = item.tot_S + last_item.sold
                                item.remaining_S = item.remaining_S + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'M':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_M:
                                    item.remaining_M = item.remaining_M - last_item.sold
                                    print('M rimanenti =',  item.remaining_M)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_M == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_M = item.tot_M + last_item.sold
                                item.remaining_M = item.remaining_M + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'L':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_L:
                                    item.remaining_L = item.remaining_L - last_item.sold
                                    print('L rimanenti =',  item.remaining_L)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_L == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_L = item.tot_L + last_item.sold
                                item.remaining_L = item.remaining_L + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'XL':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_XL:
                                    item.remaining_XL = item.remaining_XL - last_item.sold
                                    print('XL rimanenti =',  item.remaining_XL)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_XL == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_XL = item.tot_XL + last_item.sold
                                item.remaining_XL = item.remaining_XL + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
            else:
                form_unisex = ClothingFormUnisex()
        elif b[0] == 'Woman':
            if request.method == 'POST':
                if form_woman.is_valid():
                    clothing = form_woman.save(commit=False)
                    now = datetime.datetime.now()
                    items_woman.date = now
                    clothing.save()


                last_item = items_woman.last()
                last_item.code = b[1]
                activity = b[2]
                last_item.activity = activity
                last_item.save()

                item_size = form_woman.cleaned_data.get('size')
                print('item size =', item_size )
                print('item sold =', form_woman.cleaned_data.get('sold') )

                # save the remaining size of this item
                for item in items:
                    if item.code == b[1]:
                        if item_size == 'XS':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_XS:
                                    item.remaining_XS = item.remaining_XS - last_item.sold
                                    print('XS rimanenti =',  item.remaining_XS)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_XS == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_XS = item.tot_XS + last_item.sold
                                item.remaining_XS = item.remaining_XS + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'S':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_S:
                                    item.remaining_S = item.remaining_S - last_item.sold
                                    print('S rimanenti =',  item.remaining_S)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_S == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_S = item.tot_S + last_item.sold
                                item.remaining_S = item.remaining_S + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'M':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_M:
                                    item.remaining_M = item.remaining_M - last_item.sold
                                    print('M rimanenti =',  item.remaining_M)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_M == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_M = item.tot_M + last_item.sold
                                item.remaining_M = item.remaining_M + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'L':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_L:
                                    item.remaining_L = item.remaining_L - last_item.sold
                                    print('L rimanenti =',  item.remaining_L)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_L == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_L = item.tot_L + last_item.sold
                                item.remaining_L = item.remaining_L + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
                        elif item_size == 'XL':
                            if (b[2] == 'Venduto') :
                                if last_item.sold <= item.remaining_XL:
                                    item.remaining_XL = item.remaining_XL - last_item.sold
                                    print('XL rimanenti =',  item.remaining_XL)
                                    item.save()
                                    return render(request, 'insanityApp/home.html', context)
                                elif item.remaining_XL == 0:
                                    print('non ne hai più')
                                    return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
                                else:
                                    return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')
                            else: #'Aggiungi'
                                item.tot_XL = item.tot_XL + last_item.sold
                                item.remaining_XL = item.remaining_XL + last_item.sold
                                item.save()
                                return render(request, 'insanityApp/home.html', context)
        else:
                form_woman = ClothingFormMan()

    context['items'] = items
    context['form_unisex'] = form_unisex
    context['form_woman'] = form_woman
    return render(request, 'insanityApp/woman.html', context)


def accessories(request):
    context = {}
    accessories = Accessories.objects.all()
    items = AccessoryItem.objects.all()

    form = AccessoryFormSold(request.POST)
    if request.POST:
        if form.is_valid():
            acc_form = form.save(commit=False)
            now = datetime.datetime.now()
            accessories.date = now
            acc_form.save()

            number = form.cleaned_data.get('sold')
            print('number =', number)

            a = []
            for k in request.POST:
                a.append(k)
            print('quiiiiiiiiiiiiiiiiiiii', a)
            if a != []:
                print(a[2].split(','))
                b = a[2].split(',')
                print('b[0] =', b[0])
                print('b[1] =', b[1])

                last_item = accessories.last()
                code = b[0]
                last_item.code = code
                activity = b[1]
                last_item.activity = activity
                last_item.save()

                for accessory in items:
                    if accessory.code == code:
                        if activity == 'Aggiunto':
                            print('Aggiunto')
                            accessory.tot = accessory.tot + number
                            accessory.tot_remaining = accessory.tot_remaining + number
                            accessory.save()
                        else: #Venduto
                            accessory.tot_remaining = accessory.tot_remaining - number
                            accessory.save()
                            print('venduto')

    context['form'] = form
    context['items'] = items

    return render(request, 'insanityApp/accessories.html', context)

def bracelets(request):
    return render(request, 'insanityApp/bracelets.html', {})





def check_XS(item, last_item):
    if last_item.sold <= item.remaining_XS:
        item.remaining_XS = item.remaining_XS - last_item.sold
        print('XS rimanenti =',  item.remaining_XS)
        item.save()
    elif item.remaining_XS == 0:
        print('non ne hai più')
        return HttpResponse('Attenzione! Zero articoli per questo prodotto.')
    else:
        return HttpResponse('Attenzione!Non ne hai abbastanza per venderli.')