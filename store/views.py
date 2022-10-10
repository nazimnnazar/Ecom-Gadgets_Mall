from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
# from .utils import cookieCart, cartData, guestOrder

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)