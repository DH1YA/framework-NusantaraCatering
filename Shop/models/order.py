from django.db import models
from Shop.models.user import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key unik untuk pesanan
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User yang melakukan pemesanan
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    order_time = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('delivered', 'Delivered')], default='pending')
    payment_status = models.CharField(max_length=10, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid')

    def __str__(self):
        return f"Order {self.id} by {self.user.name}"
