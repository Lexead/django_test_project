import requests
from bs4 import BeautifulSoup
from rest_framework import response, status, views, viewsets
from rest_framework.permissions import IsAuthenticated

from links.models import Collection, Link
from links.permissions import IsOwner
from links.serializers import CollectionSerializer, LinkSerializer


class LinkView(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def create(self, request, *args, **kwargs):
        input_url = request.data.get("url")
        result = requests.get(input_url)
        bs = BeautifulSoup(result.text, "html.parser")
        title = bs.find("meta", property="og:title").get("content")
        description = bs.find("meta", property="og:description").get("content")
        url = bs.find("meta", property="og:url").get("content")
        image_url = bs.find("meta", property="og:image").get("content")
        og_type = bs.find("meta", property="og:type").get("content")

        if og_type.startswith("music"):
            type = "music"
        elif og_type.startswith("video"):
            type = "video"
        elif og_type.startswith("article"):
            type = "article"
        elif og_type.startswith("book"):
            type = "book"
        else:
            type = "website"

        link = Link.objects.create(
            title=title, description=description, url=url, image_url=image_url, type=type, user=request.user
        )

        serializer = self.get_serializer(link)
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CollectionView(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
