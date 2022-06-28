from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Usercrowd(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email =models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField( max_length=11, blank=True)
    profile_img = models.ImageField(upload_to='images/')
    is_active =models.BooleanField(default=False)
    expire_date = models.DateTimeField()



