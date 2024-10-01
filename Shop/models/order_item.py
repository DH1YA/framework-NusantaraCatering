from django.db import models
from .order import Order
from .menu import Menu

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Item terkait dengan pesanan
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # Menu yang dipesan
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.menu.name} in order {self.order.id}"
