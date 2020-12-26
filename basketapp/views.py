from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from mainapp.models import Product
from basketapp.models import Basket


@login_required
def basket_add(request, id=None):
    product = get_object_or_404(Product, id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    def basket_add_quantity():
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        return basket_add_quantity()

    else:
        basket = baskets.first()
        return basket_add_quantity()


@login_required
def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket = Basket.objects.get(id=int(id))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets
        }
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
