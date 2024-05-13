from rest_framework import serializers
from django.utils import timezone

from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "short_description", "links"]

    def create(self, validated_data):
        return Collection.objects.get_or_create(**validated_data)


class UpdateCollectionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=False)
    short_description = serializers.CharField(max_length=200, required=False)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.short_description = validated_data.get(
            "short_description", instance.short_description)
        instance.update_at = timezone.now()
        instance.save()

        return instance


class ShowCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"
