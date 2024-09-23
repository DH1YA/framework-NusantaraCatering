from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Menambahkan primary key eksplisit
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name