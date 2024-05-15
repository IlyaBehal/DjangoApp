from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<int:product_id>/', views.cart_add, name='carts_add'),
    path('cart_change/<int:product_id>/', views.cart_change, name='carts_change'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]