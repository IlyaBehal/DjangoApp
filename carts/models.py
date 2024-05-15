from django.db import models

from users.models import User
from goods.models import Products

class CartsQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartsQueryset().as_manager()

    class Meta:
        db_table = 'cart'

    def products_price(self):
        return round(self.product.sell_price() * self.quantity,2)

    def __str__(self):
        return f'Кошик {self.user.username}| товар: {self.product.name} | к-сть: {self.quantity}'
