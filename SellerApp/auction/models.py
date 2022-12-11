# Import necessary modules and packages
from django.db import models
from django.contrib.auth.models import User


# Define user model to store user information
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Define auction model to store auction information
class Auction(models.Model):
    item_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name= {self.item_name}: USerID= {self.user_id}"
