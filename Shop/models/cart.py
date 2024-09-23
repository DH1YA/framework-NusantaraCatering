from django.db import models
from Shop.models.user import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Satu user, satu keranjang
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.name}"