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


def furniture_leisure_view(request):
    furniture_leisure = Product.objects.filter(category__name="Мебель для отдыха").exclude(specialoffers__isnull=False)
    return render(request, 'index/furniture_leisure.html', {'products': furniture_leisure})


def furniture_for_work_view(request):
    furniture_for_work = Product.objects.filter(category__name="Мебель для работы").exclude(specialoffers__isnull=False)
    return render(request, 'index/furniture_for_work.html', {'products': furniture_for_work})


def furniture_kitchen_view(request):
    furniture_kitchen = Product.objects.filter(category__name="Мебель для кухни").exclude(specialoffers__isnull=False)
    return render(request, 'index/furniture_kitchen.html', {'products': furniture_kitchen})


def furniture_child_room_view(request):
    furniture_child_room = (
        Product.objects.filter(category__name="Мебель для детской").exclude(specialoffers__isnull=False)
    )
    return render(
        request,
        'index/furniture_child_room.html',
        {'products': furniture_child_room}
    )


def furniture_bathroom_view(request):
    furniture_bathroom = Product.objects.filter(category__name="Мебель для ванной").exclude(specialoffers__isnull=False)
    return render(request, 'index/furniture_bathroom.html', {'products': furniture_bathroom})
