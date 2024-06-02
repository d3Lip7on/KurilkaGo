import base64

from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

page_size = 12


def index(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def getCigarettes(request, page):
    cigarettes_page = Cigarette.objects.all()[(page - 1) * page_size: page * page_size]

    for product in cigarettes_page:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''

    prev_page = 1 if page == 1 else page - 1
    next_page = 3 if page == 3 else page + 1

    return render(request, 'products-page.html', {
        'title': 'Cigarettes',
        'products_url': '/cigarettes/',
        'products_page': page,
        'product_url': '/cigarette/',
        "products": cigarettes_page,
        'prev_page': prev_page,
        'next_page': next_page,
    })


def getCigarette(request, id):
    this_cigarette = get_object_or_404(Cigarette, id=id)
    if this_cigarette.image:
        this_cigarette.image_base64 = base64.b64encode(this_cigarette.image).decode('utf-8')
    else:
        this_cigarette.image_base64 = ''

    return render(request, 'item-page.html', {"product": this_cigarette})


def getDisposableVapes(request, page):
    disposable_vape_page = DisposableVape.objects.all()[(page - 1) * page_size: page * page_size]
    for product in disposable_vape_page:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''
    return render(request, 'products-page.html', {
        "title": 'E-Cig',
        'products_url': '/disposablevapes/',
        'products_page': page,
        'product_url': '/disposablevape/',
        "products": disposable_vape_page
    })


def getDisposableVape(request, id):
    this_disposable_vape = get_object_or_404(DisposableVape, id=id)
    if this_disposable_vape.image:
        this_disposable_vape.image_base64 = base64.b64encode(this_disposable_vape.image).decode('utf-8')
    else:
        this_disposable_vape.image_base64 = ''
    return render(request, 'item-page.html', {"product": this_disposable_vape})


def getHookahs(request, page):
    hookahs_page = Hookah.objects.all()[(page - 1) * page_size: page * page_size]
    for product in hookahs_page:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''
    return render(request, 'products-page.html', {
        'title': 'Hookah',
        'products_url': '/hookahs/',
        'products_page': page,
        'product_url': '/hookah/',
        "products": hookahs_page,
    })


def getHookah(request, id):
    this_hookah = get_object_or_404(Hookah, id=id)
    if this_hookah.image:
        this_hookah.image_base64 = base64.b64encode(this_hookah.image).decode('utf-8')
    else:
        this_hookah.image_base64 = ''
    return render(request, 'item-page.html', {"product": this_hookah})


def getIqoses(request, page):
    iqos_page = Heating.objects.all()[(page - 1) * page_size: page * page_size]
    for product in iqos_page:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''
    return render(request, 'products-page.html', {
        'title': 'Iqos',
        'products_url': '/iqoses/',
        'products_page': page,
        'product_url': '/iqos/',
        "products": iqos_page,
    })


def getIqos(request, id):
    this_iqos = get_object_or_404(Heating, id=id)
    if this_iqos.image:
        this_iqos.image_base64 = base64.b64encode(this_iqos.image).decode('utf-8')
    else:
        this_iqos.image_base64 = ''
    return render(request, 'item-page.html', {"product": this_iqos})


def getLiquids(request, page):
    liquid_page = Liquid.objects.all()[(page - 1) * page_size: page * page_size]
    for product in liquid_page:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''
    return render(request, 'products-page.html', {
        'title': 'Liquid',
        'products_url': '/liquids/',
        'products_page': page,
        'product_url': '/liquid/',
        "products": liquid_page,
    })


def getLiquid(request, id):
    this_liquid = get_object_or_404(Liquid, id=id)
    if this_liquid.image:
        this_liquid.image_base64 = base64.b64encode(this_liquid.image).decode('utf-8')
    else:
        this_liquid.image_base64 = ''
    return render(request, 'item-page.html', {"product": this_liquid})


def getVapes(request, page):
    this_vape = Vape.objects.all()[(page - 1) * page_size: page * page_size]
    for product in this_vape:
        if product.image:
            product.image_base64 = base64.b64encode(product.image).decode('utf-8')
        else:
            product.image_base64 = ''
    return render(request, 'products-page.html', {
        'title': 'Pod System',
        'products_url': '/vapes/',
        'products_page': page,
        'product_url': '/vape/',
        "products": this_vape,
    })


def getVape(request, id):
    this_vape = get_object_or_404(Vape, id=id)
    if this_vape.image:
        this_vape.image_base64 = base64.b64encode(this_vape.image).decode('utf-8')
    else:
        this_vape.image_base64 = ''

    return render(request, 'item-page.html', {"product": this_vape})
