from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

page_size = 8

def index(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def getCigarettes(request, page):

    cigarettes_page = Cigarette.objects.all()[(page - 1) * page_size: page * page_size]
    # cigarettes_page = [
    #     {
    #         'id': 1,
    #         'title': 'Malborro',
    #         'price': 10
    #     },
    #     {
    #         'id': 2,
    #         'title': 'Parlage',
    #         'price': 23
    #     },
    #     {
    #         'id': 3,
    #         'title': 'fawe',
    #         'price': 23
    #     },
    #     {
    #         'id': 4,
    #         'title': 'Pafadrlage',
    #         'price': 23
    #     },
    # ]
    return render(request, 'products-page.html', {
        'title': 'Cigarettes',
        'products_url': '/cigarettes/',
        'products_page': page,
        'product_url': '/cigarette/',
        "products": cigarettes_page,
    })


def getCigarette(request, id):
    this_cigarette = get_object_or_404(Cigarette, id=id)
    return render(request, 'item-page.html', {"product": this_cigarette})


def getDisposableVapes(request, page):

    disposable_vape_page = DisposableVape.objects.all()[(page - 1) * page_size: page * page_size]

    return render(request, 'products-page.html', {
        "title": 'E-Cig',
        'products_url': '/disposablevapes/',
        'products_page': page,
        'product_url': '/disposablevape/',
        "products": disposable_vape_page
    })


def getDisposableVape(request, id):
    this_disposable_vape = get_object_or_404(DisposableVape, id=id)
    return render(request, 'item-page.html', {"product": this_disposable_vape})


def getHookahs(request, page):

    hookahs_page = Hookah.objects.all()[(page - 1) * page_size: page * page_size]
    return render(request, 'products-page.html', {
        'title': 'Hookah',
        'products_url': '/hookahs/',
        'products_page': page,
        'product_url': '/hookah/',
        "products": hookahs_page,
    })


def getHookah(request, id):
    this_hookah = get_object_or_404(Hookah, id=id)
    return render(request, 'item-page.html', {"product": this_hookah})


def getIqoses(request, page):

    iqos_page = Heating.objects.all()[(page - 1) * page_size: page * page_size]
    return render(request, 'products-page.html', {
        'title': 'Iqos',
        'products_url': '/iqoses/',
        'products_page': page,
        'product_url': '/iqos/',
        "products": iqos_page,
    })


def getIqos(request, id):
    this_iqos = get_object_or_404(Heating, id=id)
    return render(request, 'item-page.html', {"product": this_iqos})


def getLiquids(request, page):

    liquid_page = Liquid.objects.all()[(page - 1) * page_size: page * page_size]
    return render(request, 'products-page.html', {
        'title': 'Liquid',
        'products_url': '/liquids/',
        'products_page': page,
        'product_url': '/liquid/',
        "products": liquid_page,
    })


def getLiquid(request, id):
    this_liquid = get_object_or_404(Liquid, id=id)
    return render(request, 'item-page.html', {"product": this_liquid})

def getVapes(request, page):

    this_vape = Vape.objects.all()[(page - 1) * page_size: page * page_size]
    return render(request, 'products-page.html', {
        'title': 'Vapes',
        'products_url': '/vapes/',
        'products_page': page,
        'product_url': '/vape/',
        "products": this_vape,
    })


def getVape(request, id):
    this_vape = get_object_or_404(Vape, id=id)
    return render(request, 'item-page.html', {"product": this_vape})
