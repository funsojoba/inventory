from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

ROLES = (
    ('admin', 'admin'),
    ('creator', 'creator'),
    ('sales', 'sales')
)


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True')
        
        if not email:
            raise ValueError('Email field is required')
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    class User(AbstractBaseUser, PermissionsMixin):
        fullname = models.CharField(max_length=200)
        email = models.EmailField(unique=True)
        role = models.CharField(choices=ROLES, max_length=10)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        
        USERNAME_FIELD = 'email'
        object = CustomUserManager()
        
        def __str__(self):
            return self.email
        
        class Meta:
            ordering = ('-created_at')
        
