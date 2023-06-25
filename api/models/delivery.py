from django.db import models
from api.models import Order, User
from .base_model import BaseModel

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('en_route', 'En route'),
        ('completed', 'Completed'),
    ]

class Delivery(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Delivery {self.id}"
