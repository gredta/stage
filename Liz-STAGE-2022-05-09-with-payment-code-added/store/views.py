from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

# Create your views here.

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def favorites(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        favorite, created = Favorite.objects.get_or_create(customer=customer, complete=False)
        items = favorite.favoriteitem_set.all()
    else:
        items = []
        favorite = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'favorite':favorite}
    return render(request, 'store/favorites.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def orderplaced(request):
    return render(request, 'store/orderplaced.html')

def history(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        favorite, created = favorite.objects.get_or_create(customer=customer, complete=False)
        items = favorite.favoriteitem_set.all()
    else:
        items = []
        favorite = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'favorite':favorite}
    return render(request, 'store/history.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def updateItem1(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    favorite, created = Favorite.objects.get_or_create(customer=customer, complete=False)

    favoriteItem, created = FavoriteItem.objects.get_or_create(order=favorite, product=product)
    
    favoriteItem.save()
    
    return JsonResponse('Item was added', safe=False)