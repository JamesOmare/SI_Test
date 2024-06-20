from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, username, email, password = None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        
        # This sets the email to lowercase
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(username = username, email = email)
        user.set_password(password)
        user.save()
        
        return user
        
    def create_superuser(self, username, email, password = None):
        if password is None:
            raise TypeError('Password should not be none')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
       
       

class UserData(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True, db_index = True)
    email = models.EmailField(max_length = 255, unique = True, db_index = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # attributes user will use to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email