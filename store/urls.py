from . import views
from django.urls import path



app_name = 'store'

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('customer/<int:customer_id>', views.customer, name='customer'),

    path('customer_profile', views.customer_profile, name='customer_profile'),
    path('customer_orders', views.customer_orders, name='customer_orders'),
    path('products', views.products, name='products'),

    path('create_order/<int:customer_id>', views.create_order, name='create_order'),
    path('update_order/<int:order_id>', views.update_order, name='update_order'),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),

]

