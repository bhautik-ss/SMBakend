# ****************** Django's Libraries ******************* 
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login

# ******************** Serializers and Models *****************
from employee.serializers import EmployeeSerializer, EmployeeRegisterSerializer
from employee.models import *
from employee.permissions import UpdateEmployeeProfile

# ****************** Rest Libraries **********************
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated

# ******************* knox ***************************
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView



# Create your views here.
class EmployeeRegisterApiView(APIView):
    serializer_class = EmployeeRegisterSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.password = make_password(self.request.data["password"])
            user.save()
            token = AuthToken.objects.create(user)[1]
            return Response({'message': 'You are registered successfully..!','token':token})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print("Serializer data--",request.data)
        serializer = AuthTokenSerializer(data=request.data)
        print("USER--",serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApiView, self).post(request, format=None)

class EmployeeApiViewSet(viewsets.ModelViewSet):
    """ Handle updatig profile """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateEmployeeProfile,IsAuthenticated,)
    serializer_class = EmployeeSerializer
    queryset = employeeProfile.objects.all()