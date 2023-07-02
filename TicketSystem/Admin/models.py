from django.db import models

# Create your models here.
class Admin(models.Model):
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    

class Department(models.Model):
    Name = models.CharField(max_length=10)
    Description = models.CharField(max_length=50)
    created_by = models.CharField(max_length=20)
    Created_at =  models.DateTimeField(auto_now_add=True)
    Last_Update_at =  models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
