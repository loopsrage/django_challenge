from . import models


class ExpertsMeta:
    """Meta data for Experts model"""
    model = models.Experts
    fields = [
        'first_name',
        'last_name',
        'short_url',
        'friends',
    ]
