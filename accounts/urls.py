from django.urls import path, include

from accounts.views import *


urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path(
        'register/',
        AuthViewSet.as_view({'post': 'register'}),
        name='register'
    ),
    path(
        'change_password/',
        AuthViewSet.as_view({'post': 'change_password'}),
        name='change_password'
    ),
    path('logout/', AuthViewSet.as_view({'post': 'logout'}), name='logout'),
    path(
        'api/password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')),
]
