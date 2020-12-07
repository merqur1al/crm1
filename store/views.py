from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import OrderForm, CustomerProfileForm
from .filters import OrderFilter
from users.decorators import allow_to_view, admin_only


def customer_profile(request):
    customer = request.user.customer
    form = CustomerProfileForm(instance=customer)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form,
               'customer':customer}
    return render(request, 'store/customerProfile.html', context)

@login_required(login_url='users:login')
@allow_to_view(allowed_roles=['customer'])
def customer_orders(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered_orders = orders.filter(status='Delivered').count()
    pending_orders = orders.filter(status='Pending').count()

    context = {'customer':customer,
               'orders':orders,
               'total_orders':total_orders,
               'delivered_orders':delivered_orders,
               'pending_orders':pending_orders
               }
    return render(request, 'store/customerOrders.html', context)

@login_required(login_url='users:login')
@admin_only
def dashboard(request):
    orders = Order.objects.order_by('-date_created')[:5]
    orders_count = Order.objects.all()
    total_orders = orders_count.count()
    delivered_orders = orders_count.filter(status='Delivered').count()
    pending_orders = orders_count.filter(status='Pending').count()

    customers = Customer.objects.all()

    context = {'customers':customers,
               'orders':orders,
               'total_orders':total_orders,
               'delivered_orders':delivered_orders,
               'pending_orders':pending_orders,
               }
    return render(request, 'store/dashboard.html', context)

@login_required(login_url='users:login')
@allow_to_view(allowed_roles=['admin'])
def customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    order_count = orders.count()

    context = {'customer':customer,
               'myFilter':myFilter,
               'orders':orders,
               'order_count':order_count,
               }
    return render(request, 'store/customer.html', context)

@allow_to_view(allowed_roles=['customer'])
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return  render(request, 'store/products.html', context)

@login_required(login_url='users:login')
def create_order(request, customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=7)
    customer = Customer.objects.get(id=customer_id)
    #form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset,
               'customer':customer
               }
    return render(request, 'store/create_order.html', context)

@login_required(login_url='users:login')
@allow_to_view(allowed_roles=['admin'])
def update_order(request, order_id):
    order = Order.objects.get(id=order_id)

    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'store/update_order.html', context)

@login_required(login_url='users:login')
@allow_to_view(allowed_roles=['admin'])
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order':order}
    return render(request, 'store/delete_order.html', context)


