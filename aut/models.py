from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
 
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)

    phone_no = models.CharField(
        max_length=15, 
        validators=[RegexValidator(r'^\d{9,15}$', 'Enter a valid phone number.')],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email