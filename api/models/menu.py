from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from api.models import Restaurant
from .base_model import BaseModel

def menu_image_upload_to(instance, filename):
    # Customize the upload path and filename for menu images
    return f'menu/{instance.restaurant.name}/{filename}'

class Menu(BaseModel):
    """
      ** Menu reprsents a menu item in a restaurant's menu. Not the entire menu book.
    price: is stored as an integer in cents. For example, $1.99 is stored as 199.
    """
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to=menu_image_upload_to)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
    class Meta:
      db_table = 'menu'
