from datetime import timedelta, datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from myapp2.models import Client, Order


# Create your views here.


def index(request):
    return render(request, 'myapp2/index.html')


def client_orders(request, id_client: int):
    products = {}

    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(client=client).all()

    for order in orders:
        products[order.id] = str(order.product.all()).replace('<QuerySet [<', '').replace('>]>',
                                                                                          '').split('>, <')

    return render(request, 'myapp2/client_orders.html', {'client': client, 'orders': orders,
                                                        'products': products})

def client_products_sorted(request, id_client: int, days: int):
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(client=client, order_date__range=(before, now)).all()
    for order in orders:
        products = order.product.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'myapp2/client_all_products_from_orders.html',
                  {'client': client, 'product_set': product_set, 'days': days})