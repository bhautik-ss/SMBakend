from rest_framework import serializers
from employee import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.employee
        fields = ["id", "fname", "lname", "email", "emp_type", "contact_number", "date_of_joinig"]

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    fname = serializers.CharField(required=True, style={'input_type':'text', 'placeholder':'First Name'})
    lname = serializers.CharField(required=True, style={'input_type':'text', 'placeholder':'Last Name'})
    email = serializers.CharField(required=True, style={'input_type':'email', 'placeholder':'Email'})
    password = serializers.CharField(required=True, style={'input_type':'password', 'placeholder':'Password'})
    class Meta:
        model = models.employee
        fields = ["id", "fname", "lname", "email", "password","emp_type", "contact_number", "date_of_joinig"]