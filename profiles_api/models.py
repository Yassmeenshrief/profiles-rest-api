from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#a5r 3 import dol 3shan a3rf ast5dm ll models l gahza 3la tol


# Create your models here.
class UserProfileManager(BaseUserManager):
    """manager for user profiles"""
    def create_user(self,email,name, password = None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress')

        email = self.normalize_email(email)
        user = self.models(email = email, name=name)
        user.setpassword(password)
        user.save(using = self._db)
        return user

    def Create_Superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin ):
    """Database model for users in the system """
    #line 8 dh yosta7sn yt3ml b3d kol class aw function 3shan a3rf hya bt3ml eh bzbt esmo dog string
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELD = ['name']

    def get_full_name (self):
        """Retrieve full name of the user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name
    def __str__ (self):
        """returning the represntation of our user"""
        return self.email
