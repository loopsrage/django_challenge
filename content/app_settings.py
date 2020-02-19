from . import models


class ContentMeta:
    """Meta data for Content model"""
    model = models.Content
    fields = [
        'name',
        'url',
        'description',
        'status',
        'expert_id',
    ]


class ContentHeadersMeta:
    """Meta data for Content headers model"""
    model = models.ContentHeader
    fields = [
        'header_text',
        'content_id',
    ]