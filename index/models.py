from django.db import models
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length =30)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.name