from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {
        'title': 'Товары',
        'products': Product.objects.all(),
        'products_category': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)
