from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from hospitals.models import Hospital

AUTH_PROVIDERS = {
    'email': 'email', 'google': 'google', 'twitter': 'twitter', 'facebook': 'facebook'
}


class UserManager(BaseUserManager):

    def _create_user(self, phone, password, auth_provider=AUTH_PROVIDERS.get('email'), **extra_fields):

        user = self.model(
            phone=phone,
            auth_provider=auth_provider,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            phone=phone,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser):
    username = None
    name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Mobile number', unique=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(default="Male", max_length=6)
    status = models.CharField(max_length=20, default="Online", blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    auth_provider = models.CharField(max_length=255, blank=True, null=True, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'age', 'gender']

    objects = UserManager()

    def __str__(self):
        return self.phone

    # for checking permissions to keep. All admins have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # does this user have permissions to view the app
    def has_module_perms(self, app_label):
        return True


class Doctor(models.Model):
    doctor = models.ForeignKey(User, related_name='doctor', on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, related_name='hospital', on_delete=models.CASCADE)
