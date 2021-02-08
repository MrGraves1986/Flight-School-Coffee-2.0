from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Coffees, Sizes, Styles, Customers, SingleCartItems, TotalCartItems

# mira add on's
from django.http import JsonResponse
import json
from .models import Product, Order
###

def index(request):
    return render(request,'index.html')

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
     return render(request, 'about.html')

def current_roasts(request):
    context = {
        'current_roasts':Coffees.objects.filter(status="current")
    }
    return render(request, 'current_roasts.html', context)

def upcoming_roasts(request):
    context = {
        'upcoming_roasts':Coffees.objects.filter(status="upcoming")
    }
    return render(request, 'upcoming_roasts.html', context)

def view_roast(request, roast_id):
    context = {
        'this_roast':Coffees.objects.get(id=roast_id),
        'all_sizes': Sizes.objects.all(),
        'all_styles': Styles.objects.all()
    }
    return render(request, 'view_roast.html', context)

def add_to_cart(request, roast_id):
    if request.method == 'POST':
        cost = request.POST['cost']
        per_pound = Sizes.objects.get(id=request.POST['ordered_size'])
        order_price = cost * per_pound.order_size
        SingleCartItems.objects.create(
            ordered_coffee=Coffees.objects.get(id=request.POST['ordered_coffee']),
            ordered_style=Styles.objects.get(id=request.POST['ordered_style']),
            ordered_size=Sizes.objects.get(id=request.POST['ordered_size']),
            order_price=order_price
        )
        return redirect('/current_roasts')
    else:
        return redirect(f'/{roast_id}/view_roast')

def submit_mail(request):
    return render (request, "success.html")

def back_home(request):
    return render (request, "index.html")


# paypal
def store(request):
	products = Product.objects.all()
	context = {'products':products}

	return render(request, 'paypal/store.html', context)

def checkout(request, pk):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	
	return render(request, 'paypal/checkout.html', context)

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
		)

	return JsonResponse('Payment completed!', safe=False)