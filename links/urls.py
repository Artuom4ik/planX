from django.urls import path

from .views import *

urlpatterns = [
    path('', LinksViewSet.as_view({
        'post': 'create'
    }), name='link-list'),
    path('<int:pk>/', LinksViewSet.as_view({
        'get': 'get_link',
        'put': 'update',
        'delete': 'delete'
    }), name='link-detail'),
]
