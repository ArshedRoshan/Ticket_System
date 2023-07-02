from django.db import models
from django.contrib.auth.models import AbstractUser
from Admin.models import Department
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,phone_number=None, password=None,**extra_fields):
        if not email and not phone_number:
            raise ValueError('At least one of email or phone number must be provided')

        
        user = self.model(
           
            email = email,
            phone_number=phone_number,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20,unique=True)
    phone_number = models.CharField(max_length=11,unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['phone_number']
    # EMAIL_FIELD = 'Email'

    objects = MyAccountManager()
    

class Tickets(models.Model):
    Subject = models.CharField(max_length = 20)
    Body = models.TextField()
    Priority = models.CharField(max_length=10)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=11)
    
    

