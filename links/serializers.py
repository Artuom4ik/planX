import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['link',]

    def create(self, validated_data):
        url = validated_data.get('link')

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "lxml")

        fields = {
            "og:title": "",
            "og:description": "",
            "og:image": "",
            "og:type": ""
        }

        for field in fields:
            if soup.find("meta", property=field):
                fields[field] = soup.find("meta", property=field)['content']

        if not fields['og:title']:
            fields['og:title'] = soup.title

        if not fields["og:description"]:
            fields["og:description"] = soup.find(
                'meta', name='description')['content']

        return Link.objects.get_or_create(
            link=url,
            user=self.context['request'].user,
            defaults={
                "title": fields["og:title"],
                "short_description": fields["og:description"],
                "image": fields["og:image"],
                "link_type": fields["og:type"],

            }
        )



class UpdateLinkSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=False)
    short_description = serializers.CharField(max_length=200, required=False)
    link = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Link
        fields = [
            "id",
            "title",
            "short_description",
            "link",
            "image",
            "link_type"
        ]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.short_description = validated_data.get(
            "short_description",
            instance.short_description
        )
        instance.link = validated_data.get("link", instance.link)
        instance.image = validated_data.get("image", instance.image)
        instance.link_type = validated_data.get(
            "link_type",
            instance.link_type
        )
        instance.update_at = timezone.now()
        instance.save()

        return instance


class ShowLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
