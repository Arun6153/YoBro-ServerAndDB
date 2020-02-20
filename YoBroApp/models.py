from django.db import models

# Create your models here.
class User(models.Model):
    Email=models.TextField()
    Password=models.TextField()
    Address=models.TextField()
