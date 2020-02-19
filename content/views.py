from uuid import uuid4
from urllib.parse import urlparse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from scrapyd_api import ScrapydAPI
from django.shortcuts import get_object_or_404
from . import serializers
from . import models

# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')


class ContentViewSet(ModelViewSet):
    """Viewset for CRUD functionality of Content objects"""
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()

    @action(detail=True, methods=['post', 'get', ])
    def parse_headers(self, request, pk=None):
        """Uses the url of the content object and uses it as a starting point
        For a spider configured to retrieve h1-3 tags"""
        content_object = get_object_or_404(models.Content, pk=pk)

        unique_id = str(uuid4())
        domain = urlparse(content_object.url).netloc

        settings= {
            'unique_id': unique_id,
            'content_object': pk
        }
        task = scrapyd.schedule(
            'default',
            'headerspider',
            settings=settings,
            url=content_object.url,
            domain=domain,
        )
        content_object.task_id = task
        content_object.save()
        return Response({'task_id': task, 'unique_id': unique_id, 'status': 'Started'})


class ContentHeaderViewSet(ModelViewSet):
    """Viewset for content headers"""
    serializer_class = serializers.ContentHeaderSerializer
    queryset = models.ContentHeader.objects.all()