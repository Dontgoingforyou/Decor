from django.urls import path
from index.apps import IndexConfig
from index.views import index, catalog

app_name = IndexConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
]
