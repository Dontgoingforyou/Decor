from django.shortcuts import render

from .models import SpecialOffers, Product


def index_view(request):
    special_offers = SpecialOffers.objects.order_by('created_at')[:3]
    latest_products = Product.objects.exclude(specialoffers__isnull=False).order_by('created_at')[:6]
    return render(
        request,
        'index/index.html',
        {'special_offers': special_offers, 'latest_products': latest_products})


def catalog_view(request):
    products = Product.objects.exclude(specialoffers__isnull=False).all()
    return render(request, 'index/catalog.html', {'products': products})


