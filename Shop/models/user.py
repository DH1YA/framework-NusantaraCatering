from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)  # Unik dan menjadi primary key
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email