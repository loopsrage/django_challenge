
from django.db import models
from experts import models as expert_models

# Create your models here.

STARTED = 1
FINISHED = 2
STATUSES = (
    (STARTED, 'Started'),
    (FINISHED, 'Finished'),
)


class Content(models.Model):
    """References an Expert and associates them with the content."""
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    url = models.URLField()

    description = models.TextField()

    # Cascade delete because content from an expert that no longer exists should not be retained
    expert_id = models.ForeignKey(expert_models.Experts, on_delete=models.CASCADE)

    # Keep track of web crawler status
    status = models.IntegerField(choices=STATUSES)

    # Crawler task ID
    task_id = models.CharField(max_length=255)

    def __str__(self):
        """Overwrite str to print the friendly name of the content object"""
        return self.name


class ContentHeader(models.Model):
    """Model for storing instances of h1-3 tags from crawled sites"""
    id = models.AutoField(primary_key=True)

    unique_id = models.CharField(max_length=100, null=True)
    header_text = models.TextField()

    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """Overwrite str to print the header_text attribute"""
        return self.header_text

