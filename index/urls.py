from django.urls import path
from django.views.generic.base import RedirectView
from index.apps import IndexConfig
from index.views import index_view, catalog_view, furniture_leisure_view, furniture_kitchen_view, \
    furniture_child_room_view, furniture_bathroom_view, furniture_for_work_view

app_name = IndexConfig.name

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico'), name='favicon'),
    path('', index_view, name='index'),
    path('catalog/', catalog_view, name='catalog'),
    path('furniture_leisure/', furniture_leisure_view, name='furniture_leisure'),
    path('furniture_for_work/', furniture_for_work_view, name='furniture_for_work'),
    path('furniture_kitchen/', furniture_kitchen_view, name='furniture_kitchen'),
    path('furniture_child_room/', furniture_child_room_view, name='furniture_child_room'),
    path('furniture_bathroom/', furniture_bathroom_view, name='furniture_bathroom'),
]
