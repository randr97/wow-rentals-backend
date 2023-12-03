from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.TextChoices):
    INDIVIDUAL = "I", _("INDIVIDUAL")
    CORPORATE = "C", _("CORPORATE")


class EmailUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    customer_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    user_type = models.CharField(
        max_length=1, choices=UserType.choices,
        null=False,
        blank=False
    )

    address_street = models.CharField(max_length=100, null=False, blank=False)
    address_city = models.CharField(max_length=100, null=False, blank=False)
    address_state = models.CharField(max_length=100, null=False, blank=False, choices=settings.STATE_CHOICES)
    address_zipcode = models.CharField(max_length=100, null=False, blank=False)

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone',
        'first_name',
        'last_name',
        'password',
        'user_type',
        'address_street', 'address_city', 'address_state', 'address_zipcode'
    ]

    def __str__(self):
        return self.email
