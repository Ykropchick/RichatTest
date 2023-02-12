import stripe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item


def canceled(request):
    return render(request, 'payment/cancel.html')


def success(request):
    return render(request, 'payment/success.html')


def items(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'payment/items.html', context=context)


def item(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item': item,
    }
    return render(request, 'payment/item.html', context=context)


def buy(request, id):
    item = Item.objects.get(pk=id)
    stripe.api_key = 'sk_test_51Mak8SI9WrAPPkvtbea4ED9qEOwzuc2WcH4j1b0Kefv4t9on7canraY0sV4w5LuDApLAoyGPJrQp07XrnjLmqJ1q009aWjN9Bx'
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/canceled',
    )
    return redirect(session.url)