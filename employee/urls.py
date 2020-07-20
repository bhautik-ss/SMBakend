from django.urls import path, include
from employee.views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views

app_name = "employee"

router = DefaultRouter()
router.register('', EmployeeApiViewSet),

urlpatterns = [
    path('api/register/', EmployeeRegisterApiView.as_view(), name="employee_register"),
    path('api/api-token-auth/', views.obtain_auth_token, name="api_auth_token"),
    path('', LoginApiView.as_view(), name="login"),
    path('api/employee/', include(router.urls)),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
