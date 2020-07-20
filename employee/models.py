from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

# Create your models here.
class employeeProfileManager(BaseUserManager):
    """ Manager for e,ployee profiles """
    def create_user(self, email, password=None):
        """ Create a new employee profile """
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        return user

    def create_superuser(self, email, password):
        """ Create and save a new superuser with given credentials """
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user

class employeeProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for employees in the system """
    emp_type = [
        ("1","Project Manager"),
        ("2","Bidding Manager"),
        ("3","Senior Project Manager"),
        ("4","Accountant Executive"),
        ("5","Panel Manager"),
        ("6","Sales Executive"),
        ("7","Leadership"),
    ]
    state = [
        ("guj", "Gujarat"),
        ("raj", "Rajsthan"),
        ("mp", "Madhyapradesh"),
        ("mh", "Maharashtra"),
        ("dl", "Delhi"),
        ("pj", "Punjab"),
    ]
    email = models.EmailField(null=False, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
    emp_type = models.CharField(choices=emp_type, default="1", max_length=3)
    contact_number = models.CharField(max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Contact number must be in the format of '+123456789'. Up to 13 digits allowed.")])
    date_of_joinig = models.DateField(auto_now_add=True, editable=True)
    address1 = models.CharField(max_length=100, null=False)
    address2 = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(choices=state, max_length=3)
    zipcode = models.CharField(max_length=6, validators=[RegexValidator(regex=r'^\d{4,6}$', message="Zipcode invalid")])
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = employeeProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_lable):
        return True

    def __str__(self):
        """ Return string representation of our employee """
        return self.email