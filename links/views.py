from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Link
from .serializers import LinkSerializer, UpdateLinkSerializer, ShowLinkSerializer


class LinksViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = LinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        link = get_object_or_404(Link, pk=pk)
        serializer = ShowLinkSerializer(link)
        return Response(serializer.data)

    def update(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Link.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
 
        serializer = UpdateLinkSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response({"link": serializer.data})

    def destroy(self, request, pk=None):
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            link = Link.objects.get(pk=pk)
            link.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except:
            return Response({"error": "Object does not exists"})
