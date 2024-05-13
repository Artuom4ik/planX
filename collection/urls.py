from django.urls import path

from .views import *

urlpatterns = [
    path('', CollectionsViewSet.as_view({
        'post': 'create'
    }), name='link-list'),
    path('<int:pk>/', CollectionsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='link-detail'),
]
