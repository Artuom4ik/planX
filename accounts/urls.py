from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from accounts.views import *


urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', AuthViewSet.as_view({'post': 'register'}), name='register'),
    path('changepassword/', AuthViewSet.as_view({'post': 'change_password'}), name='change_password'),
    path('logout/', AuthViewSet.as_view({'post': 'logout'}), name='logout'),
]
