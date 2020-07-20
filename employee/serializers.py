from rest_framework import serializers
from employee import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.employeeProfile
        fields = ["id", "first_name", "last_name", "email", "emp_type", "contact_number", "date_of_joinig", "address1", "address2", "city", "state", "zipcode"]

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, style={'input_type':'text', 'placeholder':'First Name'})
    last_name = serializers.CharField(required=True, style={'input_type':'text', 'placeholder':'Last Name'})
    email = serializers.CharField(required=True, style={'input_type':'email', 'placeholder':'Email'})
    password = serializers.CharField(required=True, style={'input_type':'password', 'placeholder':'Password'})
    date_of_joinig = serializers.DateField(required=True)
    class Meta:
        model = models.employeeProfile
        fields = ["id", "first_name", "last_name", "email", "password","emp_type", "contact_number", "date_of_joinig", "address1", "address2", "city", "state", "zipcode"]