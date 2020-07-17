from django.urls import path
from employee.views import *
from rest_framework.authtoken import views

app_name = "employee"

urlpatterns = [
    path('', EmployeeApiView.as_view(), name="employee_view"),
    path('api/register/', EmployeeRegisterApiView.as_view(), name="employee_register"),
    path('api/api-token-auth/', views.obtain_auth_token, name="api_auth_token")
]
