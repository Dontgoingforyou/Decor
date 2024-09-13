from django.urls import path
from index.apps import IndexConfig
from index.views import index

app_name = IndexConfig.name

urlpatterns = [
    path('', index, name='index')
]
