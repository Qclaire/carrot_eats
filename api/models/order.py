from django.db import models
from .base_model import BaseModel

status_choices = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]



class Order(BaseModel):
    customer = models.ForeignKey("api.User", on_delete=models.CASCADE)
    menu = models.ForeignKey("api.Menu", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=status_choices)

    def __str__(self):
        return f"Order {self.id}"
