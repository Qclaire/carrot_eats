from django.db import models
from django.core.validators import MinLengthValidator
from api.models import User
from .base_model import BaseModel

class Restaurant(BaseModel):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    description = models.TextField()
    owner = models.ForeignKey("api.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
      db_table = 'restaurant'

