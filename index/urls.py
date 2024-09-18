from django.urls import path
from index.apps import IndexConfig
from index.views import index_view, catalog_view

app_name = IndexConfig.name

urlpatterns = [
    path('', index_view, name='index'),
    path('catalog/', catalog_view, name='catalog'),
]
