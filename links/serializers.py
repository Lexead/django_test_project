from rest_framework import serializers

from links.models import Collection, Link


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Link
        fields = ("title", "description", "url", "image_url", "type", "user")


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    links = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all())

    class Meta:
        model = Collection
        fields = ("name", "description", "links", "user")
