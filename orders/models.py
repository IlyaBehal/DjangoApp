from django.db import models

from goods.models import Products
from users.models import User

class OrderItemQuerySet(models.QuerySet):
        
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        
        return 0


class Order(models.Model):

    class Meta:
        db_table = 'order'

    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    created_timestamp = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(null=True, blank=True, default=None)
    payment_on_get = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="В обробці")

    def __str__(self):
        return f'Заказ №{self.pk} | покупець {self.user.first_name} {self.user.last_name}'
    

class OrderItem(models.Model):

    class Meta:
        db_table = 'order_item'

    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, default=None)
    name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_timestamp = models.DateField(auto_now_add=True)

    objects = OrderItemQuerySet().as_manager()

    def __str__(self):
        return f'Заказ №{self.order.pk} | товар {self.product.name}'
    
    def products_price(self):
        return round(self.price * self.quantity,2)
    

