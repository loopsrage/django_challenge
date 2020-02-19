from rest_framework import serializers
from . import app_settings


class ContentSerializer(serializers.ModelSerializer):
    """Serializer class for Content Viewset"""

    class Meta(app_settings.ContentMeta):
        """Inherits from app_settings ContentMeta"""
        pass


class ContentHeaderSerializer(serializers.ModelSerializer):
    """Serializer class for content headers
    """

    class Meta(app_settings.ContentHeadersMeta):
        """Inherits from app_settings ContentHeadersMeta"""
        pass
