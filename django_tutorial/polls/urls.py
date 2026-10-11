from django_urls import path
from . import viems


urlpatterns = [
    path('', viems.index, name="index"),
    path('vsem_privet', viems.vsem_privet, name="vsem_privet")
]