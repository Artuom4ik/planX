from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Collection
from .serializers import *


class CollectionsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = CollectionSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            link = Collection.objects.get(pk=pk)
            serializer = ShowCollectionsSerializer(link)
            return Response(serializer.data)

        except Collection.DoesNotExist:
            return Response({"error": "Object does not exists"})

    def update(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        instance = Collection.objects.get(pk=pk)

        serializer = UpdateCollectionSerializer(
            data=request.data,
            instance=instance
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"link": serializer.data})

    def destroy(self, request, pk=None):
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            link = Collection.objects.get(pk=pk)
            link.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Collection.DoesNotExist:
            return Response({"error": "Object does not exists"})
