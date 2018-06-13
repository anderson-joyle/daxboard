import uuid

from django.db import models

# Create your models here.
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Session(Common):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expires_on = models.DateTimeField()
    token = models.TextField()
    tenant = models.CharField(max_length=128)
    resource = models.URLField(max_length=256)
    client_id = models.CharField(max_length=60)

    # def __str__(self):
    #     return 'test'