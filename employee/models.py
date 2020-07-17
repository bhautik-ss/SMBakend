from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class employee(models.Model):
    emp_type = [
        ("1", "Demo"),
        ("2", "Manager"),
        ("3", "Director"),
        ("4", "Sales Person"),
    ]
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100, null=False)
    emp_type = models.CharField(choices=emp_type, default="1", max_length=3)
    contact_number = models.CharField(max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Contact number must be in the format of '+123456789'. Up to 13 digits allowed.")])
    date_of_joinig = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)