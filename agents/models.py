from django.db import models
from django.conf import settings

# Create your models here.

class Agents(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sector = models.CharField(max_length=255,default='customer_support')
    ratings = models.DecimalField(decimal_places=2,max_digits=3,default=5.00)
