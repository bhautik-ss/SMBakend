from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from employee.serializers import EmployeeSerializer, EmployeeRegisterSerializer
from employee.models import *

# Create your views here.
class EmployeeApiView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request):
        emp_obj = employee.objects.all()
        serializer = self.serializer_class(emp_obj, many=True)
        return Response(serializer.data)

class EmployeeRegisterApiView(APIView):
    serializer_class = EmployeeRegisterSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.password = make_password(self.request.data["password"])
            user = serializer.save()
            # token = AuthToken.objects.create(user)
            return Response({'message': 'You are registered successfully..!','token':token})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)