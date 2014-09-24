from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from mainview.models import Column

# Create your models here.

class UserManagers(BaseUserManager):
    def create_user(self, Email, uName, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not Email:
            raise ValueError('Users must have an email address')

        user = self.model(
            Email=UserManagers.normalize_email(Email),
            uName = uName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, uName, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(Email,
            uName = uName,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Roles(models.Model):
    Id = models.AutoField(primary_key=True)
    rName = models.CharField(max_length=128)
    Power = models.ManyToManyField(Column, related_name='RolesPowers')

    def __unicode__(self):
        return str(Id)

class Users(AbstractBaseUser):
    Email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    uName = models.CharField(max_length=256, unique=True)
    #uPass = models.CharField(max_length=70)
    Role = models.ManyToManyField(Roles, related_name='UserRoles')
    exPower = models.ManyToManyField(Column, related_name='UserPowers')
    Telephone = models.CharField(max_length=16, null=True)
    Addr = models.CharField(max_length=256, null=True)
    Postcode = models.CharField(max_length=8, null=True)
    Province = models.CharField(max_length=8, null=True)
    Addtime = models.DateField(auto_now_add=True)
    Lastlogon = models.DateTimeField(null=True)
    Check = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManagers()
    
    USERNAME_FIELD = 'uName'
    REQUIRED_FIELDS = ['Email']

    class Meta:
        app_label = 'adminxxzx'

    def get_full_name(self):
        # The user is identified by their email address
        return self.Name

    def get_short_name(self):
        # The user is identified by their email address
        return self.Name

    def __unicode__(self):
        return self.uName

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True

    def __unicode__(self):
        return str(Id)
