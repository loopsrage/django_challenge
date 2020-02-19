from rest_framework import serializers
from . import app_settings


class ExpertSerializer(serializers.ModelSerializer):
    """Serializer class for Content Viewset"""

    class Meta(app_settings.ExpertsMeta):
        """Inherits from app_settings ContentMeta"""
        pass
