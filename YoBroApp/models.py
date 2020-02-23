from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'Receiver')
    messages = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

class Group_members(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    members = models.ForeignKey(User, on_delete=models.CASCADE)