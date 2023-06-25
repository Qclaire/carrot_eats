from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models

from api.permissions import Roles

from .base_model import BaseModel


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)




class User(AbstractUser, BaseModel):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()
    username = None
    is_active = models.BooleanField(default=True)

    first_name = models.CharField(
        max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255, validators=[
                                 MinLengthValidator(2)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    role = models.CharField(max_length=255, default='CUSTOMER', choices=((_.upper(), _.lower()) for _ in Roles))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'
    
    def save(self, *args, **kwargs):
        self.is_active = True
        super(User, self).save(*args, **kwargs)
        
