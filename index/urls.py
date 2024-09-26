from django.urls import path
from django.views.generic.base import RedirectView
from index.apps import IndexConfig
from index.views import index_view, catalog_view, products_by_category_view

app_name = IndexConfig.name

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico'), name='favicon'),
    path('', index_view, name='index'),
    path('catalog/', catalog_view, name='catalog'),
    path('furniture_leisure/', products_by_category_view, {'category_name': 'Мебель для отдыха', 'page_title': 'Мебель для отдыха', 'header_class': 'top-leisure'}, name='furniture_leisure'),
    path('furniture_for_work/', products_by_category_view, {'category_name': 'Мебель для работы', 'page_title': 'Мебель для работы', 'header_class': 'top-work'}, name='furniture_for_work'),
    path('furniture_kitchen/', products_by_category_view, {'category_name': 'Мебель для кухни', 'page_title': 'Мебель для кухни', 'header_class': 'top-kitchen'}, name='furniture_kitchen'),
    path('furniture_child_room/', products_by_category_view, {'category_name': 'Мебель для детской', 'page_title': 'Мебель для детской', 'header_class': 'top-child-room'}, name='furniture_child_room'),
    path('furniture_bathroom/', products_by_category_view, {'category_name': 'Мебель для ванной', 'page_title': 'Мебель для ванной', 'header_class': 'top-bathroom'}, name='furniture_bathroom'),
]
