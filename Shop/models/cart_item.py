from django.db import models
from Shop.models.menu import Menu
from Shop.models.cart import Cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')  # Hubungan ke keranjang
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # Foreign Key ke model Menu
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.menu.name}"